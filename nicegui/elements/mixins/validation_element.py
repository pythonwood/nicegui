from typing import Any, Callable, Dict, Optional

from .value_element import ValueElement


class ValidationElement(ValueElement):

    def __init__(self, validation: Dict[str, Callable[..., bool]], **kwargs: Any) -> None:
        throttle = kwargs.pop('throttle', 0.3)
        leading_events = kwargs.pop('leading_events', False)
        trailing_events = kwargs.pop('trailing_events', True)
        super().__init__(throttle=throttle, leading_events=leading_events, trailing_events=trailing_events, **kwargs)
        self.validation = validation
        self._error: Optional[str] = None

    @property
    def error(self) -> Optional[str]:
        """The latest error message from the validation functions."""
        return self._error

    def on_value_change(self, value: Any) -> None:
        super().on_value_change(value)
        for message, check in self.validation.items():
            if not check(value):
                self._error = message
                self.props(f'error error-message="{message}"')
                break
        else:
            self._error = None
            self.props(remove='error')
