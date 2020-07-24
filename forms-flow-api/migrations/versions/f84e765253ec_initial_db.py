"""initial-db

Revision ID: f84e765253ec
Revises: 
Create Date: 2020-06-15 16:46:59.123742

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f84e765253ec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('application_audit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('application_id', sa.Integer(), nullable=True),
    sa.Column('application_name', sa.String(length=100), nullable=False),
    sa.Column('application_status', sa.String(length=10), nullable=False),
    sa.Column('form_process_mapper_id', sa.Integer(), nullable=False),
    sa.Column('form_submission_id', sa.String(length=30), nullable=False),
    sa.Column('process_instance_id', sa.String(length=30), nullable=False),
    sa.Column('revision_no', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('form_io_token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('keycloak_role', sa.String(length=50), nullable=False),
    sa.Column('formio_token', sa.String(length=500), nullable=False),
    sa.Column('formio_role', sa.String(length=50), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('form_process_mapper',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.String(), nullable=False),
    sa.Column('modified_by', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('form_id', sa.String(length=50), nullable=False),
    sa.Column('form_name', sa.String(length=100), nullable=False),
    sa.Column('form_revision_number', sa.String(length=10), nullable=False),
    sa.Column('process_key', sa.String(length=50), nullable=False),
    sa.Column('process_name', sa.String(length=100), nullable=False),
    sa.Column('status', sa.String(length=10), nullable=False),
    sa.Column('comments', sa.String(length=300), nullable=True),
    sa.Column('tenant_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tenant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tenant_name', sa.String(), nullable=False),
    sa.Column('relam', sa.String(), nullable=False),
    sa.Column('audience', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('application',
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('created_by', sa.String(), nullable=False),
    sa.Column('modified_by', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('application_name', sa.String(length=100), nullable=False),
    sa.Column('application_status', sa.String(length=10), nullable=False),
    sa.Column('form_process_mapper_id', sa.Integer(), nullable=False),
    sa.Column('form_submission_id', sa.String(length=30), nullable=False),
    sa.Column('process_instance_id', sa.String(length=30), nullable=False),
    sa.Column('revision_no', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['form_process_mapper_id'], ['form_process_mapper.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('application_communication',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('application_id', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(length=3000), nullable=False),
    sa.Column('created_by', sa.String(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['application_id'], ['application.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('application_communication')
    op.drop_table('application')
    op.drop_table('tenant')
    op.drop_table('form_process_mapper')
    op.drop_table('form_io_token')
    op.drop_table('application_audit')
    # ### end Alembic commands ###
