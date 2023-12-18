from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DayOfTheWeek(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUN: _ClassVar[DayOfTheWeek]
    MON: _ClassVar[DayOfTheWeek]
    TUE: _ClassVar[DayOfTheWeek]
    WED: _ClassVar[DayOfTheWeek]
    THU: _ClassVar[DayOfTheWeek]
    FRI: _ClassVar[DayOfTheWeek]
    SAT: _ClassVar[DayOfTheWeek]
SUN: DayOfTheWeek
MON: DayOfTheWeek
TUE: DayOfTheWeek
WED: DayOfTheWeek
THU: DayOfTheWeek
FRI: DayOfTheWeek
SAT: DayOfTheWeek

class OperatingInfo(_message.Message):
    __slots__ = ("open_day_of_the_week", "open_hour", "close_day_of_the_week", "close_hour")
    OPEN_DAY_OF_THE_WEEK_FIELD_NUMBER: _ClassVar[int]
    OPEN_HOUR_FIELD_NUMBER: _ClassVar[int]
    CLOSE_DAY_OF_THE_WEEK_FIELD_NUMBER: _ClassVar[int]
    CLOSE_HOUR_FIELD_NUMBER: _ClassVar[int]
    open_day_of_the_week: DayOfTheWeek
    open_hour: str
    close_day_of_the_week: DayOfTheWeek
    close_hour: str
    def __init__(self, open_day_of_the_week: _Optional[_Union[DayOfTheWeek, str]] = ..., open_hour: _Optional[str] = ..., close_day_of_the_week: _Optional[_Union[DayOfTheWeek, str]] = ..., close_hour: _Optional[str] = ...) -> None: ...

class CafeDetail(_message.Message):
    __slots__ = ("name", "address", "rating", "operating_info")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    OPERATING_INFO_FIELD_NUMBER: _ClassVar[int]
    name: str
    address: str
    rating: float
    operating_info: _containers.RepeatedCompositeFieldContainer[OperatingInfo]
    def __init__(self, name: _Optional[str] = ..., address: _Optional[str] = ..., rating: _Optional[float] = ..., operating_info: _Optional[_Iterable[_Union[OperatingInfo, _Mapping]]] = ...) -> None: ...

class CafeUpdateRequest(_message.Message):
    __slots__ = ("name", "address", "rating", "operating_info", "is_address_null", "is_rating_null", "is_operating_info_null")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    OPERATING_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_ADDRESS_NULL_FIELD_NUMBER: _ClassVar[int]
    IS_RATING_NULL_FIELD_NUMBER: _ClassVar[int]
    IS_OPERATING_INFO_NULL_FIELD_NUMBER: _ClassVar[int]
    name: str
    address: str
    rating: float
    operating_info: _containers.RepeatedCompositeFieldContainer[OperatingInfo]
    is_address_null: bool
    is_rating_null: bool
    is_operating_info_null: bool
    def __init__(self, name: _Optional[str] = ..., address: _Optional[str] = ..., rating: _Optional[float] = ..., operating_info: _Optional[_Iterable[_Union[OperatingInfo, _Mapping]]] = ..., is_address_null: bool = ..., is_rating_null: bool = ..., is_operating_info_null: bool = ...) -> None: ...

class AllCafeReply(_message.Message):
    __slots__ = ("cafes",)
    CAFES_FIELD_NUMBER: _ClassVar[int]
    cafes: _containers.RepeatedCompositeFieldContainer[CafeDetail]
    def __init__(self, cafes: _Optional[_Iterable[_Union[CafeDetail, _Mapping]]] = ...) -> None: ...

class CafeName(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class UserId(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class CouponDetail(_message.Message):
    __slots__ = ("cafe_name", "count")
    CAFE_NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    cafe_name: str
    count: int
    def __init__(self, cafe_name: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class CouponDetailReply(_message.Message):
    __slots__ = ("is_success", "coupon_detail")
    IS_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    COUPON_DETAIL_FIELD_NUMBER: _ClassVar[int]
    is_success: bool
    coupon_detail: CouponDetail
    def __init__(self, is_success: bool = ..., coupon_detail: _Optional[_Union[CouponDetail, _Mapping]] = ...) -> None: ...

class AllCouponReply(_message.Message):
    __slots__ = ("is_success", "coupons")
    IS_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    COUPONS_FIELD_NUMBER: _ClassVar[int]
    is_success: bool
    coupons: _containers.RepeatedCompositeFieldContainer[CouponDetail]
    def __init__(self, is_success: bool = ..., coupons: _Optional[_Iterable[_Union[CouponDetail, _Mapping]]] = ...) -> None: ...

class CouponRequest(_message.Message):
    __slots__ = ("user_id", "cafe_name")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CAFE_NAME_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    cafe_name: str
    def __init__(self, user_id: _Optional[int] = ..., cafe_name: _Optional[str] = ...) -> None: ...

class EmptyRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EmptyReply(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CUDReply(_message.Message):
    __slots__ = ("is_success",)
    IS_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    is_success: bool
    def __init__(self, is_success: bool = ...) -> None: ...

class CouponUseReply(_message.Message):
    __slots__ = ("find_success", "use_success")
    FIND_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    USE_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    find_success: bool
    use_success: bool
    def __init__(self, find_success: bool = ..., use_success: bool = ...) -> None: ...

class CouponData(_message.Message):
    __slots__ = ("name", "count")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    name: str
    count: int
    def __init__(self, name: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class CouponRankingReply(_message.Message):
    __slots__ = ("is_success", "coupon_datas")
    IS_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    COUPON_DATAS_FIELD_NUMBER: _ClassVar[int]
    is_success: bool
    coupon_datas: _containers.RepeatedCompositeFieldContainer[CouponData]
    def __init__(self, is_success: bool = ..., coupon_datas: _Optional[_Iterable[_Union[CouponData, _Mapping]]] = ...) -> None: ...
