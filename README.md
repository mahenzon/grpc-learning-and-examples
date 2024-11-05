- настроили Poetry
- установили Python пакет `protobuf`
- поставили protobuf на macOS командой
    ```shell
    brew install protobuf
    ```
  

## Протокол Ping

- описали протокол
- компилируем командой
    ```shell
    protoc --python_out=./pb protos/ping.proto
    ```
- инициализируем экземпляр в коде и назначаем свойства:
    ```python
    from pb.protos import ping_pb2

    ping = ping_pb2.Ping()
    ping.ok = True
    print("ping:", ping.SerializeToString())
    ```
- ставим дополнительно пакет `mypy-protobuf`: https://github.com/nipunn1313/mypy-protobuf
- теперь компилируем с доп флагом:
    ```shell
    protoc --python_out=./pb --mypy_out=./pb protos/ping.proto
    ``` 
- теперь mypy не ругается
- сделали запись в файл
- прочитали данные из файла в экземпляр
- проверили `ping.IsInitialized()`


## Протокол User
- описали протокол `User`, использовали разные типы, перешли на `proto3`, добавили `enum`
- компилируем с доп флагом:
    ```shell
    protoc --python_out=./pb --mypy_out=./pb protos/user.proto
    ``` 
  


## Протокол UserResponse
- избавились от плагина mypy-protobuf
- стали использовать параметр `--pyi_out=`
- также поправили себя по передаче `--proto_path=PATH`, стали вызывать так:
    ```shell
    protoc --proto_path=protos --python_out=./pb --pyi_out=./pb protos/*
    ``` 
- осталось страдание с импортами, не поправлено и не планируется: https://github.com/protocolbuffers/protobuf/issues/1491
  просто исправляем вручную на `from . import aaa_pb2`
- описали сущности



## Сервис UserGetter
- описываем сервис
- описываем прото запроса и ответа
- ставим пакет `grpcio`
- компилим всё как обычно:
    ```shell
    protoc --proto_path=protos --python_out=./pb --pyi_out=./pb protos/*
    ```
- плюс компилируем **только сервис протоколы** с флагом grpc:
    ```shell
    python -m grpc_tools.protoc --proto_path=protos --python_out=./pb --grpc_python_out=./pb --pyi_out=./pb protos/*-service.proto
    ``` 
- описываем Servicer - наследуемся от скомпиленного и реализуем `rpc` методы
- описываем старт сервера
- описываем клиент, готовим stub, делаем запросы
