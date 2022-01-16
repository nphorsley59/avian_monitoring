

import pandas as pd
import pandera as pa
from pandera.typing import DateTime


from config import Config


class DataFrameValidator:
    """Docstring"""
    def __init__(self, df: pd.DataFrame, schema: str):
        """Docstring"""
        self.df = df
        self.schema = schema

    @staticmethod
    def point_count_schema():
        """Docstring"""
        schema = pa.DataFrameSchema({
            'site_id': pa.Column(str, pa.Check.isin(Config.SITES)),
            'date': pa.Column(DateTime),
            'start_time': pa.Column(float, nullable=True),
            'point': pa.Column(float, pa.Check.in_range(Config.POINTS_RANGE['min'], Config.POINTS_RANGE['max'])),
            'minute': pa.Column(float,
                                pa.Check.in_range(Config.MINUTES_RANGE['min'], Config.MINUTES_RANGE['max']),
                                nullable=True),
            'distance': pa.Column(float,
                                  pa.Check.in_range(Config.DISTANCE_RANGE['min'], Config.DISTANCE_RANGE['max']),
                                  nullable=True),
            'how': pa.Column(str, pa.Check.isin(Config.HOW), nullable=True),
            'visual': pa.Column(bool),
            'sex': pa.Column(str, pa.Check.isin(Config.SEX)),
            'migrating': pa.Column(bool),
            'cluster_size': pa.Column(float, pa.Check.in_range(Config.CLUSTER_SIZE['min'], Config.CLUSTER_SIZE['max'])),
            'cluster_code': pa.Column(str, nullable=True),
            'notes': pa.Column(str, nullable=True),
            'observer_id': pa.Column(str, pa.Check.isin(Config.OBSERVERS))
        })
        return schema

    def validate(self):
        """Docstring"""
        if self.schema == 'point count':
            point_count_schema = self.point_count_schema()
            point_count_schema(self.df)
        else:
            raise KeyError(f'Invalid schema "{self.schema}"')


def factory():
    """Docstring"""
    pass


if __name__ == '__main__':
    factory()