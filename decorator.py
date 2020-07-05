def header(function):
    def decorator(*args, **kwargs):
        print("### BEM VINDO AO MEU SITE ### \n")
        return function(*args, **kwargs)
    return decorator


def footer(function):
    def decorator(*args, **kwargs):
        print("### COPYRIGHT - 2020 ###")
        return function(*args, **kwargs)
    return decorator 


@footer
@header
def produto(nome):
    print(f"Produto: {nome} - R$ 2k")


produto("Cadeira gamer")