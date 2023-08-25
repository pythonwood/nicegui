from typing import Any, Callable, Optional

from .mixins.disableable_element import DisableableElement
from .mixins.value_element import ValueElement


class Slider(ValueElement, DisableableElement):

    def __init__(self, *,
                 min: float,
                 max: float,
                 step: float = 1.0,
                 value: Optional[float] = None,
                 on_change: Optional[Callable[..., Any]] = None,
                 **kwargs: Any,
                 ) -> None:
        """Slider

        :param min: lower bound of the slider
        :param max: upper bound of the slider
        :param step: step size
        :param value: initial value to set position of the slider
        :param on_change: callback which is invoked when the user releases the slider
        """
        throttle = kwargs.pop('throttle', 0.05)
        leading_events = kwargs.pop('leading_events', False)
        trailing_events = kwargs.pop('trailing_events', True)
        super().__init__(tag='q-slider', value=value, on_value_change=on_change,
                         throttle=throttle, leading_events=leading_events, trailing_events=trailing_events, **kwargs)
        self._props['min'] = min
        self._props['max'] = max
        self._props['step'] = step
