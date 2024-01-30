# generated by datamodel-codegen:
#   filename:  v2.json
#   timestamp: 2024-01-30T15:09:41+00:00

from __future__ import annotations

# from dataclasses import dataclass
from datetime import date, datetime
from enum import Enum
from typing import Optional

from pydantic.dataclasses import dataclass


class Provisioner(Enum):
    k8s_pod = "k8s-pod"
    k8s_neonvm = "k8s-neonvm"


@dataclass
class Pagination:
    cursor: str


@dataclass
class EmptyResponse:
    pass


@dataclass
class ApiKeyCreateRequest:
    key_name: str


@dataclass
class ApiKeyCreateResponse:
    id: int
    key: str
    name: str
    created_at: datetime


@dataclass
class ApiKeyRevokeResponse:
    id: int
    name: str
    revoked: bool
    last_used_from_addr: str
    last_used_at: Optional[datetime] = None


@dataclass
class ApiKeysListResponseItem:
    id: int
    name: str
    created_at: datetime
    last_used_from_addr: str
    last_used_at: Optional[datetime] = None


class OperationAction(Enum):
    create_compute = "create_compute"
    create_timeline = "create_timeline"
    start_compute = "start_compute"
    suspend_compute = "suspend_compute"
    apply_config = "apply_config"
    check_availability = "check_availability"
    delete_timeline = "delete_timeline"
    create_branch = "create_branch"
    tenant_ignore = "tenant_ignore"
    tenant_attach = "tenant_attach"
    tenant_detach = "tenant_detach"
    tenant_reattach = "tenant_reattach"
    replace_safekeeper = "replace_safekeeper"
    disable_maintenance = "disable_maintenance"
    apply_storage_config = "apply_storage_config"


class OperationStatus(Enum):
    running = "running"
    finished = "finished"
    failed = "failed"
    scheduling = "scheduling"


@dataclass
class Branch:
    name: Optional[str] = None
    role_name: Optional[str] = None
    database_name: Optional[str] = None


@dataclass
class ProjectPermission:
    id: str
    granted_to_email: str
    granted_at: datetime
    revoked_at: Optional[datetime] = None


@dataclass
class ProjectPermissions:
    project_permissions: list[ProjectPermission]


@dataclass
class GrantPermissionToProjectRequest:
    email: str


@dataclass
class ProjectConsumption:
    project_id: str
    period_id: str
    data_storage_bytes_hour: int
    synthetic_storage_size: int
    data_transfer_bytes: int
    written_data_bytes: int
    compute_time_seconds: int
    active_time_seconds: int
    updated_at: datetime
    period_start: datetime
    period_end: datetime
    previous_period_id: str
    data_storage_bytes_hour_updated_at: Optional[datetime] = None
    synthetic_storage_size_updated_at: Optional[datetime] = None
    data_transfer_bytes_updated_at: Optional[datetime] = None
    written_data_bytes_updated_at: Optional[datetime] = None
    compute_time_seconds_updated_at: Optional[datetime] = None
    active_time_seconds_updated_at: Optional[datetime] = None


@dataclass
class Limits:
    active_time: int
    max_projects: int
    max_branches: int
    max_autoscaling_cu: float
    cpu_seconds: int
    max_active_endpoints: int
    max_read_only_endpoints: int
    max_allowed_ips: int


@dataclass
class ProjectLimits:
    limits: Limits


class BranchState(Enum):
    init = "init"
    ready = "ready"


@dataclass
class Branch2:
    parent_id: Optional[str] = None
    name: Optional[str] = None
    parent_lsn: Optional[str] = None
    parent_timestamp: Optional[str] = None


@dataclass
class Branch3:
    name: Optional[str] = None


@dataclass
class BranchUpdateRequest:
    branch: Branch3


@dataclass
class ConnectionParameters:
    database: str
    password: str
    role: str
    host: str
    pooler_host: str


@dataclass
class ConnectionDetails:
    connection_uri: str
    connection_parameters: ConnectionParameters


class EndpointState(Enum):
    init = "init"
    active = "active"
    idle = "idle"


class EndpointType(Enum):
    read_only = "read_only"
    read_write = "read_write"


class EndpointPoolerMode(Enum):
    transaction = "transaction"


@dataclass
class AllowedIps:
    primary_branch_only: bool
    ips: Optional[list[str]] = None


@dataclass
class ConnectionURIsResponse:
    connection_uris: list[ConnectionDetails]


@dataclass
class ConnectionURIsOptionalResponse:
    connection_uris: Optional[list[ConnectionDetails]] = None


@dataclass
class EndpointPasswordlessSessionAuthRequest:
    session_id: str


Duration = int


@dataclass
class StatementData:
    truncated: bool
    fields: Optional[list[str]] = None
    rows: Optional[list[list[str]]] = None


@dataclass
class ExplainData:
    QUERY_PLAN: str


@dataclass
class Role:
    branch_id: str
    name: str
    created_at: datetime
    updated_at: datetime
    password: Optional[str] = None
    protected: Optional[bool] = None


@dataclass
class Role1:
    name: str


@dataclass
class RoleCreateRequest:
    role: Role1


@dataclass
class RoleResponse:
    role: Role


@dataclass
class RolesResponse:
    roles: list[Role]


@dataclass
class RolePasswordResponse:
    password: str


class Brand(Enum):
    amex = "amex"
    diners = "diners"
    discover = "discover"
    jcb = "jcb"
    mastercard = "mastercard"
    unionpay = "unionpay"
    unknown = "unknown"
    visa = "visa"


@dataclass
class PaymentSourceBankCard:
    last4: str
    brand: Optional[Brand] = None
    exp_month: Optional[int] = None
    exp_year: Optional[int] = None


@dataclass
class PaymentSource:
    type: str
    card: Optional[PaymentSourceBankCard] = None


@dataclass
class BillingAccount1:
    email: Optional[str] = None


@dataclass
class BillingAccountUpdateRequest:
    billing_account: BillingAccount1


class BillingSubscriptionType(Enum):
    UNKNOWN = "UNKNOWN"
    free = "free"
    pro = "pro"
    direct_sales = "direct_sales"
    aws_marketplace = "aws_marketplace"
    free_v2 = "free_v2"
    launch = "launch"
    scale = "scale"


@dataclass
class Database:
    id: int
    branch_id: str
    name: str
    owner_name: str
    created_at: datetime
    updated_at: datetime


@dataclass
class Database1:
    name: str
    owner_name: str


@dataclass
class DatabaseCreateRequest:
    database: Database1


@dataclass
class Database2:
    name: Optional[str] = None
    owner_name: Optional[str] = None


@dataclass
class DatabaseUpdateRequest:
    database: Database2


@dataclass
class DatabaseResponse:
    database: Database


@dataclass
class DatabasesResponse:
    databases: list[Database]


@dataclass
class CurrentUserAuthAccount:
    email: str
    image: str
    login: str
    name: str
    provider: str


@dataclass
class UpdateUserInfoRequest:
    email: str
    id: str
    image: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None


@dataclass
class ProjectQuota:
    active_time_seconds: Optional[int] = None
    compute_time_seconds: Optional[int] = None
    written_data_bytes: Optional[int] = None
    data_transfer_bytes: Optional[int] = None
    logical_size_bytes: Optional[int] = None


@dataclass
class HealthCheck:
    status: str


@dataclass
class ProjectOwnerData:
    email: str
    branches_limit: int
    subscription_type: BillingSubscriptionType


class SupportTicketSeverity(Enum):
    low = "low"
    normal = "normal"
    high = "high"
    critical = "critical"


@dataclass
class PaginationResponse:
    pagination: Optional[Pagination] = None


@dataclass
class Operation:
    id: str
    project_id: str
    action: OperationAction
    status: OperationStatus
    failures_count: int
    created_at: datetime
    updated_at: datetime
    total_duration_ms: int
    branch_id: Optional[str] = None
    endpoint_id: Optional[str] = None
    error: Optional[str] = None
    retry_at: Optional[datetime] = None


@dataclass
class OperationResponse:
    operation: Operation


@dataclass
class OperationsResponse:
    operations: list[Operation]


@dataclass
class ProjectSettingsData:
    quota: Optional[ProjectQuota] = None
    allowed_ips: Optional[AllowedIps] = None
    enable_logical_replication: Optional[bool] = None


@dataclass
class ProjectsConsumptionResponse:
    projects: list[ProjectConsumption]
    periods_in_response: int


@dataclass
class Branch1:
    id: str
    project_id: str
    name: str
    current_state: BranchState
    creation_source: str
    primary: bool
    cpu_used_sec: int
    compute_time_seconds: int
    active_time_seconds: int
    written_data_bytes: int
    data_transfer_bytes: int
    created_at: datetime
    updated_at: datetime
    parent_id: Optional[str] = None
    parent_lsn: Optional[str] = None
    parent_timestamp: Optional[str] = None
    pending_state: Optional[BranchState] = None
    logical_size: Optional[int] = None
    last_reset_at: Optional[datetime] = None


@dataclass
class BranchCreateRequestEndpointOptions:
    type: EndpointType
    autoscaling_limit_min_cu: Optional[float] = None
    autoscaling_limit_max_cu: Optional[float] = None
    provisioner: Optional[Provisioner] = None
    suspend_timeout_seconds: Optional[int] = None


@dataclass
class BranchCreateRequest:
    endpoints: Optional[list[BranchCreateRequestEndpointOptions]] = None
    branch: Optional[Branch2] = None


@dataclass
class BranchResponse:
    branch: Branch1


@dataclass
class BranchesResponse:
    branches: list[Branch1]


@dataclass
class StatementResult:
    query: str
    data: Optional[StatementData] = None
    error: Optional[str] = None
    explain_data: Optional[list[ExplainData]] = None


@dataclass
class BillingAccount:
    payment_source: PaymentSource
    subscription_type: BillingSubscriptionType
    quota_reset_at_last: datetime
    email: str
    address_city: str
    address_country: str
    address_line1: str
    address_line2: str
    address_postal_code: str
    address_state: str
    orb_portal_url: Optional[str] = None


@dataclass
class BillingAccountResponse:
    billing_account: BillingAccount


@dataclass
class CurrentUserInfoResponse:
    active_seconds_limit: int
    billing_account: BillingAccount
    auth_accounts: list[CurrentUserAuthAccount]
    email: str
    id: str
    image: str
    login: str
    name: str
    last_name: str
    projects_limit: int
    branches_limit: int
    max_autoscaling_limit: float
    plan: str
    compute_seconds_limit: Optional[int] = None


@dataclass
class EndpointSettingsData:
    pg_settings: Optional[dict[str, str]] = None
    pgbouncer_settings: Optional[dict[str, str]] = None


@dataclass
class DefaultEndpointSettings:
    pg_settings: Optional[dict[str, str]] = None
    pgbouncer_settings: Optional[dict[str, str]] = None
    autoscaling_limit_min_cu: Optional[float] = None
    autoscaling_limit_max_cu: Optional[float] = None
    suspend_timeout_seconds: Optional[int] = None


@dataclass
class GeneralError:
    code: str
    message: str


@dataclass
class BranchOperations(BranchResponse, OperationsResponse):
    pass


@dataclass
class DatabaseOperations(DatabaseResponse, OperationsResponse):
    pass


@dataclass
class RoleOperations(RoleResponse, OperationsResponse):
    pass


@dataclass
class ProjectListItem:
    id: str
    platform_id: str
    region_id: str
    name: str
    provisioner: Provisioner
    pg_version: int
    proxy_host: str
    branch_logical_size_limit: int
    branch_logical_size_limit_bytes: int
    store_passwords: bool
    active_time: int
    cpu_used_sec: int
    creation_source: str
    created_at: datetime
    updated_at: datetime
    owner_id: str
    default_endpoint_settings: Optional[DefaultEndpointSettings] = None
    settings: Optional[ProjectSettingsData] = None
    maintenance_starts_at: Optional[datetime] = None
    synthetic_storage_size: Optional[int] = None
    quota_reset_at: Optional[datetime] = None
    compute_last_active_at: Optional[datetime] = None


@dataclass
class Project:
    data_storage_bytes_hour: int
    data_transfer_bytes: int
    written_data_bytes: int
    compute_time_seconds: int
    active_time_seconds: int
    cpu_used_sec: int
    id: str
    platform_id: str
    region_id: str
    name: str
    provisioner: Provisioner
    pg_version: int
    proxy_host: str
    branch_logical_size_limit: int
    branch_logical_size_limit_bytes: int
    store_passwords: bool
    creation_source: str
    history_retention_seconds: int
    created_at: datetime
    updated_at: datetime
    consumption_period_start: datetime
    consumption_period_end: datetime
    owner_id: str
    default_endpoint_settings: Optional[DefaultEndpointSettings] = None
    settings: Optional[ProjectSettingsData] = None
    maintenance_starts_at: Optional[datetime] = None
    synthetic_storage_size: Optional[int] = None
    quota_reset_at: Optional[datetime] = None
    owner: Optional[ProjectOwnerData] = None
    compute_last_active_at: Optional[datetime] = None


@dataclass
class Project1:
    settings: Optional[ProjectSettingsData] = None
    name: Optional[str] = None
    branch: Optional[Branch] = None
    autoscaling_limit_min_cu: Optional[float] = None
    autoscaling_limit_max_cu: Optional[float] = None
    provisioner: Optional[Provisioner] = None
    region_id: Optional[str] = None
    default_endpoint_settings: Optional[DefaultEndpointSettings] = None
    pg_version: Optional[int] = None
    store_passwords: Optional[bool] = None
    history_retention_seconds: Optional[int] = None


@dataclass
class ProjectCreateRequest:
    project: Project1


@dataclass
class Project2:
    settings: Optional[ProjectSettingsData] = None
    name: Optional[str] = None
    default_endpoint_settings: Optional[DefaultEndpointSettings] = None
    history_retention_seconds: Optional[int] = None


@dataclass
class ProjectUpdateRequest:
    project: Project2


@dataclass
class ProjectResponse:
    project: Project


@dataclass
class ProjectsResponse:
    projects: list[ProjectListItem]


@dataclass
class Endpoint:
    host: str
    id: str
    project_id: str
    branch_id: str
    autoscaling_limit_min_cu: float
    autoscaling_limit_max_cu: float
    region_id: str
    type: EndpointType
    current_state: EndpointState
    settings: EndpointSettingsData
    pooler_enabled: bool
    pooler_mode: EndpointPoolerMode
    disabled: bool
    passwordless_access: bool
    creation_source: str
    created_at: datetime
    updated_at: datetime
    proxy_host: str
    suspend_timeout_seconds: int
    provisioner: Provisioner
    pending_state: Optional[EndpointState] = None
    last_active: Optional[str] = None


@dataclass
class Endpoint1:
    branch_id: str
    type: EndpointType
    region_id: Optional[str] = None
    settings: Optional[EndpointSettingsData] = None
    autoscaling_limit_min_cu: Optional[float] = None
    autoscaling_limit_max_cu: Optional[float] = None
    provisioner: Optional[Provisioner] = None
    pooler_enabled: Optional[bool] = None
    pooler_mode: Optional[EndpointPoolerMode] = None
    disabled: Optional[bool] = None
    passwordless_access: Optional[bool] = None
    suspend_timeout_seconds: Optional[int] = None


@dataclass
class EndpointCreateRequest:
    endpoint: Endpoint1


@dataclass
class Endpoint2:
    branch_id: Optional[str] = None
    autoscaling_limit_min_cu: Optional[float] = None
    autoscaling_limit_max_cu: Optional[float] = None
    provisioner: Optional[Provisioner] = None
    settings: Optional[EndpointSettingsData] = None
    pooler_enabled: Optional[bool] = None
    pooler_mode: Optional[EndpointPoolerMode] = None
    disabled: Optional[bool] = None
    passwordless_access: Optional[bool] = None
    suspend_timeout_seconds: Optional[int] = None


@dataclass
class EndpointUpdateRequest:
    endpoint: Endpoint2


@dataclass
class EndpointResponse:
    endpoint: Endpoint


@dataclass
class EndpointsResponse:
    endpoints: list[Endpoint]


@dataclass
class EndpointOperations(EndpointResponse, OperationsResponse):
    pass
