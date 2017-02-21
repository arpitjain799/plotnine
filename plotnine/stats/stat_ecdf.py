from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import numpy as np
import pandas as pd
from statsmodels.distributions.empirical_distribution import ECDF

from ..utils.doctools import document
from .stat import stat


@document
class stat_ecdf(stat):
    """
    Emperical Cumulative Density Function

    {usage}

    Parameters
    ----------
    {common_parameters}

    {aesthetics}

    .. rubric:: Options for computed aesthetics

    y
        - ``..x..`` - x in the data
        - ``..y..`` - cumulative density corresponding to x

    See Also
    --------
    :class:`~plotnine.geoms.geom_step`
    """
    REQUIRED_AES = {'x'}
    DEFAULT_PARAMS = {'geom': 'step', 'position': 'identity',
                      'n': None}
    DEFAULT_AES = {'y': '..y..'}
    CREATES = {'y'}

    @classmethod
    def compute_group(cls, data, scales, **params):
        # If n is None, use raw values; otherwise interpolate
        if params['n'] is None:
            x = np.unique(data['x'])
        else:
            x = np.linspace(data['x'].min(), data['x'].max(),
                            params['n'])

        y = ECDF(data['x'])(x)
        res = pd.DataFrame({'x': x, 'y': y})
        return res