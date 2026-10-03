import uuid
from datetime import datetime
from sqlalchemy import String,Text,Integer,Boolean,DateTime,UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID,JSONB
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy.sql import func
from app.db import Base
def uid():return uuid.uuid4()
class Run(Base):
 __tablename__="runs";id:Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True),primary_key=True,default=uid);tenant_id:Mapped[str]=mapped_column(String(128),index=True);principal_id:Mapped[str]=mapped_column(String(256));goal:Mapped[str]=mapped_column(Text);status:Mapped[str]=mapped_column(String(32),index=True,default="CREATED");plan:Mapped[dict|None]=mapped_column(JSONB,nullable=True)
class StepRecord(Base):
 __tablename__="steps";__table_args__=(UniqueConstraint("run_id","step_key"),);id:Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True),primary_key=True,default=uid);run_id:Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True),index=True);step_key:Mapped[str]=mapped_column(String(128));capability:Mapped[str]=mapped_column(String(256));status:Mapped[str]=mapped_column(String(32),index=True,default="PENDING");request:Mapped[dict]=mapped_column(JSONB,default=dict);response:Mapped[dict|None]=mapped_column(JSONB,nullable=True);fencing_token:Mapped[int]=mapped_column(Integer,default=0)
class Approval(Base):
 __tablename__="approvals";id:Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True),primary_key=True,default=uid);run_id:Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True),index=True);step_key:Mapped[str]=mapped_column(String(128));action_hash:Mapped[str]=mapped_column(String(64));status:Mapped[str]=mapped_column(String(32),default="PENDING")
class Outbox(Base):
 __tablename__="outbox";id:Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True),primary_key=True,default=uid);event_type:Mapped[str]=mapped_column(String(128));aggregate_id:Mapped[str]=mapped_column(String(128));payload:Mapped[dict]=mapped_column(JSONB);published:Mapped[bool]=mapped_column(Boolean,default=False,index=True)
class Idempotency(Base):
 __tablename__="idempotency";__table_args__=(UniqueConstraint("tenant_id","scope","key"),);id:Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True),primary_key=True,default=uid);tenant_id:Mapped[str]=mapped_column(String(128));scope:Mapped[str]=mapped_column(String(128));key:Mapped[str]=mapped_column(String(256));request_hash:Mapped[str]=mapped_column(String(64));result:Mapped[dict|None]=mapped_column(JSONB,nullable=True)
class Memory(Base):
 __tablename__="memory";id:Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True),primary_key=True,default=uid);tenant_id:Mapped[str]=mapped_column(String(128),index=True);layer:Mapped[str]=mapped_column(String(32));subject:Mapped[str]=mapped_column(String(256));data:Mapped[dict]=mapped_column(JSONB);revision:Mapped[int]=mapped_column(Integer,default=1)
class Audit(Base):
 __tablename__="audit";id:Mapped[uuid.UUID]=mapped_column(UUID(as_uuid=True),primary_key=True,default=uid);run_id:Mapped[uuid.UUID|None]=mapped_column(UUID(as_uuid=True),nullable=True);actor:Mapped[str]=mapped_column(String(256));event_type:Mapped[str]=mapped_column(String(128));data:Mapped[dict]=mapped_column(JSONB,default=dict);created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),server_default=func.now())
