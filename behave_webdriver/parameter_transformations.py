class NoTransformation:
    """
    Implements basic parameter transformation strategy -
    prameter is left unmodified.
    """

    def eval(self, value):
        return value


class FormatTransformation:
    """
    Implements basic interpolation transformation startegy.
    Parameter value is transformed through .format method
    using named placeholders and values supplied from the
    context passed at the time of initialization.
    """

    def __init__(self, **kwargs):
        self._context = kwargs

    def eval(self, value):
        return value.format(**self._context)


def set_context_transformation_service(context, service=NoTransformation()):
    """
    Installs parameter transformaton service into context.
    """
    setattr(context, 'parameter_transformation', service)


def transform_parameter(context, value):
    """
    Performs parameter transformation using service resolved from the context.
    If transformation service is not defined on the context (expected member
    attribute name is parameter_transformation) the it installs default
    parameter transformation service (NoTransformation).
    """
    assert context.parameter_transformation is not None
    t = getattr(context, 'parameter_transformation', NoTransformation())
    return t.eval(value)