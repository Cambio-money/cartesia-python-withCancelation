# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing
from ...embedding.types.embedding import Embedding
import typing_extensions
from .controls import ControlsParams
from ...core.serialization import FieldMetadata


class TtsRequestEmbeddingSpecifierParams(typing_extensions.TypedDict):
    mode: typing.Literal["embedding"]
    embedding: Embedding
    experimental_controls: typing_extensions.NotRequired[
        typing_extensions.Annotated[ControlsParams, FieldMetadata(alias="__experimental_controls")]
    ]
