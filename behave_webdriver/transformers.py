import os
from behave.matchers import Match, ParseMatcher, RegexMatcher, MatchWithError
from behave.matchers import matcher_mapping
from collections import defaultdict
import six

class TransformerBase(object):
    def __init__(self, context=None, func=None, **kwargs):
        self.context = context
        self.func = func

    def transform_value(self, value):
        return value

    def transform_args(self, args):
        return [self.transform_value(arg) for arg in args]

    def transform_kwargs(self, kwargs):
        return {key: self.transform_value(value) for key, value in kwargs.items()}

    def transform(self, args, kwargs):
        return self.transform_args(args), self.transform_kwargs(kwargs), self.func


class FormatTransformer(TransformerBase):
    """
    Implements basic interpolation transformation startegy.
    Parameter value is transformed through .format method
    using named placeholders and values supplied from the
    context passed at the time of initialization.
    """

    def __init__(self, context=None, func=None, **kwargs):
        suppress_missing = kwargs.pop('suppress_missing', False)
        if context is not None:
            kwargs.update(context=context)
        if func is not None:
            kwargs.update(func=func)
        super(FormatTransformer, self).__init__(**kwargs)
        self.transformations = kwargs
        if suppress_missing:
            self.transformations = defaultdict(lambda key: '', self.transformations)

    def transform_value(self, value):
        if not isinstance(value, six.string_types):
            return value  # non-string arguments should be returned unadulterated

        return value.format(**self.transformations)


class EnvironmentFormatTransformer(FormatTransformer):
    """
    Like FormatTransformer, but additionally provides items from os.environ as keyword arguments
    """
    def __init__(self, *args, **kwargs):
        kwargs.update(os.environ)
        super(EnvironmentFormatTransformer, self).__init__(*args, **kwargs)


class FuncTransformer(TransformerBase):
    """
    Replaces the step function with a supplied new function!
    """
    def __init__(self, new_func, *args, **kwargs):
        self.new_func = new_func
        super(FuncTransformer, self).__init__(*args, **kwargs)

    def transform(self, *transform_args, **transform_kwargs):
        args, kwargs, _old_func = super(FuncTransformer, self).transform(*transform_args, **transform_kwargs)
        return args, kwargs, self.new_func


class TransformingMatch(Match):
    def run(self, context):
        args = []
        kwargs = {}
        for arg in self.arguments:
            if arg.name is not None:
                kwargs[arg.name] = arg.value
            else:
                args.append(arg.value)

        with context.use_with_user_mode():
            #  the above is a COPY/PASTE of the original `run` implementation,
            # THESE next 3 lines are the key change vvv
            transformer_class = context.transformer_class if 'transformer_class' in context else None
            if transformer_class and issubclass(transformer_class, TransformerBase):
                transformer = transformer_class(context=context, func=self.func)
                args, kwargs, func = transformer.transform(args, kwargs)
            else:
                func = self.func
            func(context, *args, **kwargs)


class TransformMixin(object):
    def match(self, step):
        # -- PROTECT AGAINST: Type conversion errors (with ParseMatcher).
        try:
            result = self.check_match(step)
        except Exception as e:  # pylint: disable=broad-except
            return MatchWithError(self.func, e)

        if result is None:
            return None     # -- NO-MATCH
        #  the above is a COPY/PASTE of original implementation
        #  THIS one line is the key v
        return TransformingMatch(self.func, result)


class TransformParseMatcher(TransformMixin, ParseMatcher):
    pass


class TransformRegexMatcher(TransformMixin, RegexMatcher):
    pass

matcher_mapping['transform-parse'] = TransformParseMatcher
matcher_mapping['transform-re'] = TransformRegexMatcher
