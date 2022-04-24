# Name:
# OSU Email:
# Course: CS261 - Data Structures
# Assignment:
# Due Date:
# Description:


from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        Add a value to the bag.
        """
        self._da.append(value)


    def remove(self, value: object) -> bool:
        """
        Removes a single value taken as parameter from the Dynamic Array. If the value
        is remove, it returns True. Otherwise, it returns False.
        """
        for idx in range(self.size()):
            if self._da.get_at_index(idx) == value:
                self._da.remove_at_index(idx)
                return True
        return False

    def count(self, value: object) -> int:
        """
        Takes a value as a parameter and returns the count of the number of times
        the value is in the Dynamic Array.
        """
        count = 0
        for idx in range(self.size()):
            if self._da.get_at_index(idx) == value:
                count += 1
        return count

    def clear(self) -> None:
        """
        Clears the bag of all values in the Dynamic Array.
        """
        self._da = DynamicArray()

    def equal(self, second_bag: "Bag") -> bool:
        """
        TODO: Write this implementation
        """
        second_da = DynamicArray(second_bag)

        if self._da.length() != second_da.length():
            return False
        if self._da.is_empty() == True and second_da.is_empty() == True:
            return True

        for idx in range(self.size()):
            if self.count(self._da[idx]) != second_bag.count(self._da[idx]):
                return False

        for idx in range(second_bag.size()):
            if second_bag.count(second_da[idx]) != self.count(second_da[idx]):
                return False

        #
        # second_arr_check = second_da
        # second_count = 0
        # check = False
        # for idx in range(self._da.length()):
        #     check = False
        #     for next_idx in range(second_da.length()):
        #         if second_da[next_idx] == self._da[idx]:
        #             second_arr_check.remove_at_index(next_idx - second_count)
        #             second_count += 1
        #             check = True
        #
        #     if check == False or second_arr_check.length() != 0:
        #         return False
        #
        # first_arr_check = self._da
        # first_count = 0
        # for idx in range(second_da.length()):
        #     check = False
        #     for next_idx in range(self._da.length()):
        #         if self._da[next_idx] == second_da[idx]:
        #             first_arr_check.remove_at_index(next_idx - first_count)
        #             first_count += 1
        #             check = True
        #     if check == False or first_arr_check.length() != 0:
        #         return False


        return True

    def __iter__(self):
        """
        Creates and initializes a iterator.
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Returns the next value in the array from the interator pointer.
        """
        try:
            value = self._da[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    # print("\n# add example 1")
    #
    # bag = Bag()
    # print(bag)
    # values = [10, 20, 30, 10, 20, 30]
    # for value in values:
    #     bag.add(value)
    # print(bag)

    # print("\n# remove example 1")
    # bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    # print(bag)
    # print(bag.remove(7), bag)
    # print(bag.remove(3), bag)
    # print(bag.remove(3), bag)
    # print(bag.remove(3), bag)
    # print(bag.remove(3), bag)
    # #
    # print("\n# count example 1")
    # bag = Bag([1, 2, 3, 1, 2, 2])
    # print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))
    # #
    # print("\n# clear example 1")
    # bag = Bag([1, 2, 3, 1, 2, 3])
    # print(bag)
    # bag.clear()
    # print(bag)


    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag4 = Bag([1,2,2])
    bag5 = Bag([2,1,2])
    bag_empty = Bag()
    #
    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))
    print(bag4.equal(bag5))
    print(bag5.equal(bag4))

    # print("\n# __iter__(), __next__() example 1")
    # bag = Bag([5, 4, -8, 7, 10])
    # print(bag)
    # for item in bag:
    #     print(item)
    #
    # print("\n# __iter__(), __next__() example 2")
    # bag = Bag(["orange", "apple", "pizza", "ice cream"])
    # print(bag)
    # for item in bag:
    #     print(item)
