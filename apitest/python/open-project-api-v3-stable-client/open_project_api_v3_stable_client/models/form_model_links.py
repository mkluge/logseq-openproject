from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.form_model_links_commit import FormModelLinksCommit
    from ..models.form_model_links_preview_markup import FormModelLinksPreviewMarkup
    from ..models.form_model_links_self import FormModelLinksSelf
    from ..models.form_model_links_validate import FormModelLinksValidate


T = TypeVar("T", bound="FormModelLinks")


@attr.s(auto_attribs=True)
class FormModelLinks:
    """
    Attributes:
        validate (Union[Unset, FormModelLinksValidate]):
        commit (Union[Unset, FormModelLinksCommit]):
        preview_markup (Union[Unset, FormModelLinksPreviewMarkup]):
        self_ (Union[Unset, FormModelLinksSelf]):
    """

    validate: Union[Unset, "FormModelLinksValidate"] = UNSET
    commit: Union[Unset, "FormModelLinksCommit"] = UNSET
    preview_markup: Union[Unset, "FormModelLinksPreviewMarkup"] = UNSET
    self_: Union[Unset, "FormModelLinksSelf"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        validate: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.validate, Unset):
            validate = self.validate.to_dict()

        commit: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.commit, Unset):
            commit = self.commit.to_dict()

        preview_markup: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.preview_markup, Unset):
            preview_markup = self.preview_markup.to_dict()

        self_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if validate is not UNSET:
            field_dict["validate"] = validate
        if commit is not UNSET:
            field_dict["commit"] = commit
        if preview_markup is not UNSET:
            field_dict["previewMarkup"] = preview_markup
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.form_model_links_commit import FormModelLinksCommit
        from ..models.form_model_links_preview_markup import FormModelLinksPreviewMarkup
        from ..models.form_model_links_self import FormModelLinksSelf
        from ..models.form_model_links_validate import FormModelLinksValidate

        d = src_dict.copy()
        _validate = d.pop("validate", UNSET)
        validate: Union[Unset, FormModelLinksValidate]
        if isinstance(_validate, Unset):
            validate = UNSET
        else:
            validate = FormModelLinksValidate.from_dict(_validate)

        _commit = d.pop("commit", UNSET)
        commit: Union[Unset, FormModelLinksCommit]
        if isinstance(_commit, Unset):
            commit = UNSET
        else:
            commit = FormModelLinksCommit.from_dict(_commit)

        _preview_markup = d.pop("previewMarkup", UNSET)
        preview_markup: Union[Unset, FormModelLinksPreviewMarkup]
        if isinstance(_preview_markup, Unset):
            preview_markup = UNSET
        else:
            preview_markup = FormModelLinksPreviewMarkup.from_dict(_preview_markup)

        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, FormModelLinksSelf]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = FormModelLinksSelf.from_dict(_self_)

        form_model_links = cls(
            validate=validate,
            commit=commit,
            preview_markup=preview_markup,
            self_=self_,
        )

        form_model_links.additional_properties = d
        return form_model_links

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
