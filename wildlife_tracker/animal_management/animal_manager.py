from typing import Optional

from wildlife_tracker.animal_managment.animal import Animal

class AnimalManager:

    def __init__(self, animals: List[int] = [] ) -> None:
      self.animals: dict[int, Animal] = {}

    def get_animal_by_id(self, animal_id: int) -> Optional[Animal]:
        pass

    def register_animal(Animal) -> None:
        pass
    
    def update_animal_details(animal_id: int, **kwargs: Any) -> None:
        pass
    
    def get_animal_by_id(animal_id: int) -> Optional[Animal]:
        pass
    
    def get_animal_details(animal_id) -> dict[str, Any]:
         pass

    def remove_animal(animal_id: int) -> None:
        pass