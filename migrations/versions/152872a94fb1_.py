"""empty message

Revision ID: 152872a94fb1
Revises: 22b204ccf59d
Create Date: 2022-05-10 00:56:11.888546

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '152872a94fb1'
down_revision = '22b204ccf59d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Characters', sa.Column('birth_year', sa.String(length=120), nullable=False))
    op.add_column('Characters', sa.Column('homeworld', sa.String(length=120), nullable=False))
    op.add_column('Planets', sa.Column('name', sa.String(length=120), nullable=False))
    op.add_column('Planets', sa.Column('rotation_period', sa.String(length=120), nullable=False))
    op.add_column('Planets', sa.Column('orbital_period', sa.String(length=120), nullable=False))
    op.add_column('Planets', sa.Column('diameter', sa.String(length=120), nullable=False))
    op.add_column('Planets', sa.Column('climate', sa.String(length=120), nullable=False))
    op.add_column('Planets', sa.Column('gravity', sa.String(length=120), nullable=False))
    op.add_column('Planets', sa.Column('terrain', sa.String(length=120), nullable=False))
    op.add_column('Planets', sa.Column('surface_water', sa.String(length=120), nullable=False))
    op.add_column('Planets', sa.Column('population', sa.String(length=120), nullable=False))
    op.create_unique_constraint(None, 'Planets', ['name'])
    op.add_column('Starships', sa.Column('name', sa.String(length=120), nullable=False))
    op.add_column('Starships', sa.Column('model', sa.String(length=120), nullable=False))
    op.add_column('Starships', sa.Column('manufacturer', sa.String(length=120), nullable=False))
    op.add_column('Starships', sa.Column('cost_in_credits', sa.String(length=120), nullable=False))
    op.add_column('Starships', sa.Column('length', sa.String(length=120), nullable=False))
    op.add_column('Starships', sa.Column('max_atmosphering_speed', sa.String(length=120), nullable=False))
    op.add_column('Starships', sa.Column('crew', sa.String(length=120), nullable=False))
    op.add_column('Starships', sa.Column('passengers', sa.String(length=120), nullable=False))
    op.add_column('Starships', sa.Column('cargo_capacity', sa.String(length=120), nullable=False))
    op.add_column('Starships', sa.Column('consumables', sa.String(length=120), nullable=False))
    op.add_column('Starships', sa.Column('hyperdrive_rating', sa.String(length=120), nullable=False))
    op.add_column('Starships', sa.Column('MGLT', sa.String(length=120), nullable=False))
    op.add_column('Starships', sa.Column('starship_class', sa.String(length=120), nullable=False))
    op.add_column('Starships', sa.Column('pilots', sa.String(length=120), nullable=True))
    op.create_unique_constraint(None, 'Starships', ['name'])
    op.create_unique_constraint(None, 'Starships', ['model'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Starships', type_='unique')
    op.drop_constraint(None, 'Starships', type_='unique')
    op.drop_column('Starships', 'pilots')
    op.drop_column('Starships', 'starship_class')
    op.drop_column('Starships', 'MGLT')
    op.drop_column('Starships', 'hyperdrive_rating')
    op.drop_column('Starships', 'consumables')
    op.drop_column('Starships', 'cargo_capacity')
    op.drop_column('Starships', 'passengers')
    op.drop_column('Starships', 'crew')
    op.drop_column('Starships', 'max_atmosphering_speed')
    op.drop_column('Starships', 'length')
    op.drop_column('Starships', 'cost_in_credits')
    op.drop_column('Starships', 'manufacturer')
    op.drop_column('Starships', 'model')
    op.drop_column('Starships', 'name')
    op.drop_constraint(None, 'Planets', type_='unique')
    op.drop_column('Planets', 'population')
    op.drop_column('Planets', 'surface_water')
    op.drop_column('Planets', 'terrain')
    op.drop_column('Planets', 'gravity')
    op.drop_column('Planets', 'climate')
    op.drop_column('Planets', 'diameter')
    op.drop_column('Planets', 'orbital_period')
    op.drop_column('Planets', 'rotation_period')
    op.drop_column('Planets', 'name')
    op.drop_column('Characters', 'homeworld')
    op.drop_column('Characters', 'birth_year')
    # ### end Alembic commands ###
