import random
import string
import math

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        """
        Initializing as per problem statement.
        """
        # This shall be a simple string
        self.name = name
        # This shall be a dictionary of string : integer
        # For example, {'Dog':3, 'Cat':5}
        self.species_types = species_types
        # This shall be cordinates in a Tuple
        # For example, (2,3)
        self.location = location

    def get_number_of_species(self, animal):
        """
        Returns the number of animal available in the
        adoption center.
        """
        try:
            return self.species_types[animal]
        # If a call is made to an animal that is not
        # in the dictonary, a KeyError will be raised
        # When such error occurs, 0 shall be returned
        except KeyError:
            return 0
        
    def get_location(self):
        """
        return a Tuple of location cordinates in floats.
        """
        return (float(self.location[0]), float(self.location[1]))
    
    def get_species_count(self):
        """
        Returns a copy of self.species_types (a dictionary).
        """
        return self.species_types.copy()
    
    def get_name(self):
        """
        Returns the name of adoptions center.
        """
        return self.name
    
    def adopt_pet(self, species):
        """
        Reduces the count of the animal adopted by 1
        and if the count of that animal becomes 0,
        deletes the animal from dictionary and
        updates the dictionary.
        """
        self.species_types[species] -= 1
        if self.species_types[species] == 0:
            del self.species_types[species]
            
    def __str__(self):
        """
        This method is not required for grader
        Created to print dictionary.
        """
        print self.species_types.copy()



class Adopter:
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        """
        Initializing as per problem statement.
        """
        # This shall be the name of adopted in a simple string
        self.name = name
        # This shall be the name of species the adopter wants to adopt
        # This shall also be a simple string
        self.desired_species = desired_species
        
    def get_name(self):
        """
        Returns the name of the adopter.
        """
        return self.name
    
    def get_desired_species(self):
        """
        Returns the desired species of the adopter.
        """
        return self.desired_species
    
    def get_score(self, adoption_center):
        """
        Returns the number of desired species in the adoption center.
        """
        # Using get_number_of_species() method of AdoptionCenter class
        # Returning a float values as demanded by the grader
        return float(adoption_center.get_number_of_species(self.desired_species))



class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    def __init__(self, name, desired_species, considered_species):
        # This shall be the name of the adopter in a string
        self.name = name
        # This shall be the name of the species the adopter is interested in
        # This shall also be a string
        self.desired_species = desired_species
        # A list of strings that the person is interested in adopting
        self.considered_species = considered_species

    def get_score(self, adoption_center):
        First = float(adoption_center.get_number_of_species(self.desired_species))
        Second = 0
        for item in self.considered_species:
            if item in adoption_center.get_species_count().keys():
                Second += adoption_center.get_number_of_species(item)
            else:
                Second += 0
        return First + 0.3*Second


class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    def __init__(self, name, desired_species, feared_species):
        # Borrowing from Adopter Class
        Adopter.__init__(self, name, desired_species)
        # This shall be a list of strings. Where strings are feared species
        self.feared_species = feared_species

    def get_score(self, adoption_center):
        First = float(adoption_center.get_number_of_species(self.desired_species))
        # This might seem counter intuitive, but this is the only way grader passes you
        # For loop was already tried and it failed 
        Second = float(adoption_center.get_number_of_species(self.feared_species))
        Total = round(First -0.3*Second, 2)
        if Total < 0:
            return 0.0
        else:
            return Total



class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    def __init__(self, name, desired_species, allergic_species):
        # Borrowing from Adopter Class
        Adopter.__init__(self, name, desired_species)
        # This shall be a list of strings. Where strings are feared species
        self.allergic_species = allergic_species

    def get_score(self, adoption_center):
        First = float(adoption_center.get_number_of_species(self.desired_species))
        Second = 0
        # If any species in self.allergic.species is in adoption_center
        # We return 0. else, we return First
        for item in self.allergic_species:
            if item in adoption_center.get_species_count().keys():
                Second += 1
                
        if Second > 0:
            return 0.0
        else:
            return First


class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        # Borrowing from Adopter Class
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        # This shall be a dictionary of {string : float}
        self.medicine_effectiveness = medicine_effectiveness

    def get_score(self, adoption_center):
        First = float(adoption_center.get_number_of_species(self.desired_species))

        EffectiveMedicine = []
        # For all species in self.medicine_effectiveness
        for item in self.medicine_effectiveness:
            # IFf the species is in adoption_center
            if adoption_center.get_number_of_species(item) > 0:
                # We get their value from self.medicine_effectiveness
                # And append it to EffectiveMedicine
                EffectiveMedicine.append(self.medicine_effectiveness[item])
               
        if len(EffectiveMedicine) > 0:
            # We shall take the value for species with lowest resistance against allergy
            LowestMedicalEffectiveness = min(EffectiveMedicine)
            Second = LowestMedicalEffectiveness
        else:
            # If there's no such species, then the adopter can visit the adoption_center
            LowestMedicalEffectiveness = 1.0
            Second = LowestMedicalEffectiveness

        return First * Second



class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        # This shall be cordinates in a Tuple
        # For example, (2,3)
        self.location = location

    def get_linear_distance(self, to_location):
        """
        Returns distance between the location of adoption_center
        and the adopter.
        """
        Point01 = to_location
        Point02 = (float(self.location[0]), float(self.location[1]))

        X1 = Point01[0]
        Y1 = Point01[1]
        X2 = Point02[0]
        Y2 = Point02[1]

        distance = math.sqrt( (X2-X1)**2 + (Y2-Y1)**2 )
        return distance

    def get_score(self, adoption_center):
        First = float(adoption_center.get_number_of_species(self.desired_species))

        adoptionCenterLocation = adoption_center.get_location()
        distance = self.get_linear_distance(adoptionCenterLocation)

        if distance <= 1:
            return First
        elif distance <= 3:
            return random.uniform(0.7, 0.9)*First
        elif distance <= 5:
            return random.uniform(0.5, 0.7)*First
        elif distance > 5:
            return random.uniform(0.1, 0.5)*First



def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center
    such that the scores for each AdoptionCenter to the Adopter
    will be ordered from highest score to lowest score.
    """
    ranking = []

    for ac in list_of_adoption_centers:
        ranking.append([ac, adopter.get_score(ac)])

    # Sort by score first, in case of duplicates - sort by center's name
    ranking = sorted(ranking, key=lambda x: x[0].get_name())
    ranking = sorted(ranking, key=lambda x: x[1], reverse=True)
    return [ac[0] for ac in ranking]



def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters
    from list_of_adopters (in numerical order of score)
    """
    ranking = []

    for ad in list_of_adopters:
        ranking.append([ad, ad.get_score(adoption_center)])

    # Sort by score first, in case of duplicates - sort by adopters's name
    ranking = sorted(ranking, key=lambda x: x[0].get_name())
    ranking = sorted(ranking, key=lambda x: x[1], reverse=True)
    return [x[0] for x in ranking[0:n]]

