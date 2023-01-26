from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="WorkPackageRelationFormModel")


@attr.s(auto_attribs=True)
class WorkPackageRelationFormModel:
    """
    Example:
        {'_links': {'self': {'href': '/api/v3/relations/form'}, 'validate': {'href': '/api/v3/relations/form', 'method':
            'POST'}, 'commit': {'href': '/api/v3/relations', 'method': 'PATCH'}}, '_type': 'Form', '_embedded': {'payload':
            {'_links': {'from': {'href': '/api/v3/work_packages/4534'}, 'to': {'href': '/api/v3/work_packages/3857'}},
            '_type': 'WorkPackage', 'type': 'follows', 'delay': 3, 'description': 'let it rest for 3 days'}, 'schema':
            {'_type': 'Schema', 'id': {'name': 'ID', 'type': 'Integer', 'writable': False}, 'type': {'name': 'Type', 'type':
            'String', 'writable': True, 'allowedValues': ['relates', 'duplicates', 'duplicated', 'blocks', 'blocked',
            'precedes', 'follows', 'includes', 'partof', 'requires', 'required']}, 'reverseType': {'name': 'Reverse Type',
            'type': 'String', 'writable': False}, 'description': {'name': 'Description', 'type': 'String', 'writable':
            True}, 'from': {'_links': {'allowedValues': [{'href': '/api/v3/work_packages/{id}'}]}, 'name': 'From work
            package', 'type': 'WorkPackage', 'writable': True}, 'to': {'_links': {'allowedValues': {'href':
            '/api/v3/work_packages/{id}/available_relation_candidates', 'title': 'Available work packages to relate to'}},
            'name': 'To work package', 'type': 'WorkPackage', 'writable': True}, 'delay': {'name': 'Delay', 'type':
            'Integer', 'writable': True}}, 'validationErrors': {'from': {'_type': 'Error', 'errorIdentifier':
            'urn:openproject-org:api:v3:errors:BadExampleError', 'message': 'For the purpose of this example we need a
            validation error. The remainder of the response pretends there were no errors.'}}}}

    """

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        work_package_relation_form_model = cls()

        work_package_relation_form_model.additional_properties = d
        return work_package_relation_form_model

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
