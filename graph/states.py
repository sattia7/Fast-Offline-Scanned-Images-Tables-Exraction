from dataclasses import dataclass

@dataclass
class PipelineState:
    image: any = None
    table: any = None
    valid: bool = False
