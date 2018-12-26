import os
from behave.matchers import Match, ParseMatcher, RegexMatcher, MatchWithError
from behave.matchers import matcher_mapping
from collections import defaultdict
import six
from functools import partial

class TransformerBase(object):
    """
    Defines the basic functions of a Transformer
    As implemented, it does effectively nothing. You are meant to subclass and override the methods.

    Don't forget to call ``super`` when extending ``__init__``
    """
    def __init__(self, context=None, func=None, **kwargs):
        """

        :param context: behave context
        :param func: the matched step function currently being executed
        :param kwargs: Not doing anything with these, but allowing us to swallow them.
        """
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
    using named placeholders and values supplied as
    keyword arguments passed at the time of initialization.
    """

    def __init__(self, context=None, func=None, **kwargs):
        """

        :param context: behave context
        :param func: the matched step function currently being executed
        :param kwargs: keyword-value pairs used for formatting step strings.
        """
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


class EnvironmentTransformer(FormatTransformer):
    """
    Like FormatTransformer, but additionally provides items from ``os.environ`` as keyword arguments
    """
    def __init__(self, *args, **kwargs):
        kwargs.update(os.environ)
        super(EnvironmentTransformer, self).__init__(*args, **kwargs)


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
    """
    Tweak of the normal Match object
    When the ``transformer_class`` attribute, a subclass of ``behave_webdriver.transformers.TrransformerBase``,
    is present on the context, that class will be called with the context and decorated step function for the step
    currently being executed. This class has the ability to 'transform' the parsed arguments and the function itself.
    """
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
            transformer_class = context.transformer_class if 'transformer_class' in context else None
            if transformer_class and ((isinstance(transformer_class, partial) and issubclass(transformer_class.func, TransformerBase)) or issubclass(transformer_class, TransformerBase)):
                transformer = transformer_class(context=context, func=self.func)
                args, kwargs, func = transformer.transform(args, kwargs)
            else:
                func = self.func
            func(context, *args, **kwargs)


class TransformMixin(object):
    """
    Replaces the usual Match object with a TransformingMatch
    This can be mixed in with any matcher class and added to the mapping; you could even override existing matchers

    >>> from behave.matchers import RegexMatcher, matcher_mapping  #  any matcher will work
    >>> class TransformRegexMatcher(TransformMixin, RegexMatcher): pass
    >>> matcher_mapping['re'] = TransformRegexMatcher
    """
    def match(self, step):
        # -- PROTECT AGAINST: Type conversion errors (with ParseMatcher).
        try:
            result = self.check_match(step)
        except Exception as e:  # pylint: disable=broad-except
            return MatchWithError(self.func, e)

        if result is None:
            return None     # -- NO-MATCH
        #  the above is a COPY/PASTE of original implementation; only the following line is changed
        return TransformingMatch(self.func, result)


#  behave-webdriver uses both ParseMatcher ('parse') and RegexMatcher ('re'); so we need a transforming version of each
class TransformParseMatcher(TransformMixin, ParseMatcher):
    pass


class TransformRegexMatcher(TransformMixin, RegexMatcher):
    pass


#  add the transforming matchers to the mapping so they can be used by ``use_step_matcher``.
matcher_mapping['transform-parse'] = TransformParseMatcher
matcher_mapping['transform-re'] = TransformRegexMatcher
