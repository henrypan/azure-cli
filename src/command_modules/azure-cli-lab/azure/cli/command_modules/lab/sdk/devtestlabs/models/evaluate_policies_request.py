# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from msrest.serialization import Model


class EvaluatePoliciesRequest(Model):
    """Request body for evaluating a policy set.

    :param policies: Policies to evaluate.
    :type policies: list of :class:`EvaluatePoliciesProperties
     <azure.mgmt.devtestlabs.models.EvaluatePoliciesProperties>`
    """

    _attribute_map = {
        'policies': {'key': 'policies', 'type': '[EvaluatePoliciesProperties]'},
    }

    def __init__(self, policies=None):
        self.policies = policies
