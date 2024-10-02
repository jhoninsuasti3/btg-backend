from typing import Any, Dict, Optional

class Result:
    @classmethod
    def Ok(cls, data: Optional[Any] = None) -> Dict[str, Any]:
        return {"status": "success", "data": data}

    @classmethod
    def NotFound(cls, message: str = "Resource not found") -> Dict[str, Any]:
        return {"status": "error", "message": message}

    @classmethod
    def Conflict(cls, message: str = "Conflict occurred") -> Dict[str, Any]:
        return {"status": "error", "message": message}

    @classmethod
    def Error(cls, message: str = "An error occurred", details: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        error_response = {"status": "error", "message": message}
        if details:
            error_response["details"] = details
        return error_response
