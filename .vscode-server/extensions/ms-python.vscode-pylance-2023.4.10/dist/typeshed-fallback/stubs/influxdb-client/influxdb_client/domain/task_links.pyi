from _typeshed import Incomplete

class TaskLinks:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        _self: Incomplete | None = ...,
        owners: Incomplete | None = ...,
        members: Incomplete | None = ...,
        runs: Incomplete | None = ...,
        logs: Incomplete | None = ...,
        labels: Incomplete | None = ...,
    ) -> None: ...
    @property
    def owners(self): ...
    @owners.setter
    def owners(self, owners) -> None: ...
    @property
    def members(self): ...
    @members.setter
    def members(self, members) -> None: ...
    @property
    def runs(self): ...
    @runs.setter
    def runs(self, runs) -> None: ...
    @property
    def logs(self): ...
    @logs.setter
    def logs(self, logs) -> None: ...
    @property
    def labels(self): ...
    @labels.setter
    def labels(self, labels) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
