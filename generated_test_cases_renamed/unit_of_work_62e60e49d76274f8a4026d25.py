# Copyright (c) "Neo4j"
# Neo4j Sweden AB [https://neo4j.com]
#
# This file is part of Neo4j.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import annotations

import typing as t


if t.TYPE_CHECKING:
    import typing_extensions as te

    _T = t.TypeVar("_T")


class Query:
    """A query with attached extra data.

    This wrapper class for queries is used to attach extra data to queries
    passed to :meth:`.Session.run` and :meth:`.AsyncSession.run`, fulfilling
    a similar role as :func:`.unit_of_work` for transactions functions.

    :param text: The query text.
    :param metadata: metadata attached to the query.
    :param timeout: seconds.
    """
    def __init__(
        self,
        text: te.LiteralString,
        metadata: t.Optional[t.Dict[str, t.Any]] = None,
        timeout: t.Optional[float] = None
    ) -> None:
        self.text = text

        self.metadata = metadata
        self.timeout = timeout

    def __str__(self) -> te.LiteralString:
        return str(self.text)

#query_unit_of_work_passk_validte
<insert generated code here>


if __name__ == "__main__":
    import dill
    import os
    isT=True
    @unit_of_work(timeout=100)
    def count_people_tx(input_arg):
        return input_arg
    test_cases = dict()
    try:
        input_args="input value"
        output_args = count_people_tx(input_args)
        test_cases['test1']= input_args==output_args
    except Exception as error:
        test_cases['test1'] = type(error).__name__
    print(test_cases)




