from typing import Any, Dict, List, Union

class Base:
    PAGE = None
    
    @classmethod
    def _load(cls, **kwargs) -> List[Union[Dict[str, Any], List[None]]]:
        raise NotImplementedError
    
    @classmethod
    def get_values(cls, **kwargs) -> List[Union[Dict[str, Any], List[None]]]:
        result = cls._load(**kwargs)
        return result