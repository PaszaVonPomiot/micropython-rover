class SDBaseError(Exception): ...


class SDNotMountedError(SDBaseError): ...


class LoggerBaseError(Exception): ...


class LoggerInvalidRecordError(LoggerBaseError): ...
