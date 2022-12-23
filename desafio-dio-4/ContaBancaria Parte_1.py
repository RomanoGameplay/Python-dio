from sqlalchemy import Column, Integer, Float, String, ForeignKey, create_engine, select, func
from sqlalchemy.orm import declarative_base, relationship, Session

Base = declarative_base()


class Cliente(Base):
    __tablename__ = 'Cliente'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(9), unique=True)
    endereco = Column(String(9), unique=True)
    conta = Column(String)

    conta = relationship('Conta', back_populates='cliente', cascade='all, delete-orphan')

    def __repr__(self):
        return f'\nID: {self.id}\nNome: {self.nome}\nCPF: {self.cpf}\nEndereço: {self.endereco}\n'


class Conta(Base):
    __tablename__ = 'Conta'
    id = Column(Integer, primary_key=True)
    tipo = Column(String, default='conta_corrente')
    agencia = Column(String, default='001')
    num = Column(Integer, nullable=False, default=0)
    id_cliente = Column(Integer, ForeignKey('Cliente.id'), nullable=False)
    saldo = Column(Float, nullable=False, default=0)

    cliente = relationship('Cliente', back_populates='conta')

    def __repr__(self):
        return f'\nID: {self.id}\nTipo: {self.tipo}\nAgencia: {self.agencia}\nNumero: {self.num}\nID_Cliente: {self.id_cliente}\n'


if __name__ == '__main__':
    engine = create_engine('sqlite://')
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        Amanda = Cliente(nome='Amanda',
                         cpf='111222',
                         endereco='amandabr@gmail.com',
                         conta=[Conta(), Conta()]
                         )
        Beltrami = Cliente(nome='Beltrami',
                           cpf='222333',
                           endereco='beltramibb@gmail.com',
                           conta=[Conta()]
                           )
        Carlos = Cliente(nome='Carlos',
                         cpf='333444',
                         endereco='carlinhosbrown@gmail.com',
                         conta=[Conta()]
                         )
        Dani = Cliente(nome='Dani',
                       cpf='444555',
                       endereco='danicalabresa@gmail.com',
                       conta=[Conta()]
                       )
        Evaristo = Cliente(nome='Evaristo',
                           cpf='555666',
                           endereco='evaristocosta@gmail.com',
                           conta=[Conta()]
                           )

        session.add_all([Amanda, Beltrami, Carlos, Dani, Evaristo])
        session.commit()

    stmt_adress = select(Conta).where(Conta.id_cliente.in_([1]))
    for adress in session.scalars(stmt_adress):
        print('\t\t', adress)

    stmt_count = select(func.count('*')).select_from(Cliente)
    print('\nTotal de instâncias em Cliente:')
    for result in session.scalars(stmt_count):
        print(result)


    session.close()
