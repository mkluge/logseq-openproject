from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.formattable_format import FormattableFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProjectModelStatusExplanation")


@attr.s(auto_attribs=True)
class ProjectModelStatusExplanation:
    """
    Attributes:
        format_ (FormattableFormat): Indicates the formatting language of the raw text Example: markdown.
        raw (Union[Unset, str]): The raw text, as entered by the user Example: I **am** formatted!.
        html (Union[Unset, str]): The text converted to HTML according to the format Example: I <strong>am</strong>
            formatted!.
    """

    format_: FormattableFormat
    raw: Union[Unset, str] = UNSET
    html: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        format_ = self.format_.value

        raw = self.raw
        html = self.html

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "format": format_,
            }
        )
        if raw is not UNSET:
            field_dict["raw"] = raw
        if html is not UNSET:
            field_dict["html"] = html

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        format_ = FormattableFormat(d.pop("format"))

        raw = d.pop("raw", UNSET)

        html = d.pop("html", UNSET)

        project_model_status_explanation = cls(
            format_=format_,
            raw=raw,
            html=html,
        )

        project_model_status_explanation.additional_properties = d
        return project_model_status_explanation

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
