def print_models(unprinted_designs, completed_models):
    """Symulacja wydruku"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Wydruk modelu: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Wyswietla pozostale modele do druku"""
    print(f"Wydrukowane zostaly nastepujace modele: ")
    for completed_model in completed_models:
        print(completed_model)
