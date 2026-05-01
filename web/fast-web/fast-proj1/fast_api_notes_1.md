### Depends() Example

    def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
        return {"q": q, "skip": skip, "limit": limit}
    
    @app.get("/items/")
    async def read_items(commons: dict = Depends(common_parameters)):
        return commons

### SQLModel Example...

    # Code above omitted 👆
    from sqlmodel import Field, Session, SQLModel, create_engine, select
    
    # Code here omitted 👈
    
    class Hero(SQLModel, table=True):
        id: int | None = Field(default=None, primary_key=True)
        name: str = Field(index=True)
        secret_name: str
        age: int | None = Field(default=None, index=True)
    
    
    sqlite_file_name = "database.db"
    sqlite_url = f"sqlite:///{sqlite_file_name}"
    
    connect_args = {"check_same_thread": False}
    engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)
    
    
    def create_db_and_tables():
        SQLModel.metadata.create_all(engine)
    
    # Code below omitted 👇
