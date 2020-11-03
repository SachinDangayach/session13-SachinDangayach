# regular_poly_seq.py

from functools import lru_cache

"""Regular Polygon Sequence class"""
class RegularPolySeq:
    """Class to create a sequence of regular polygon"""

    radius = 10 # Static variable - Circumradius

    def __init__(self, vert_count):
        """Initialize the RegulaPoly class attributes"""

        self.vert_count = vert_count # Number of vertices of polygon

    @property
    def vert_count(self):
        """Get count of vertices"""
        return self._vert_count

    @vert_count.setter
    def vert_count(self, vert_count):
        """Set the number of vertices of polygon"""
        if not isinstance(vert_count, int):
            raise TypeError(f'Number of vertices should be of type integer')
        if vert_count < 3:
            raise ValueError(f'Number of vertices should be greater than or equal to 3')

        self._vert_count = vert_count

    @property
    def poly_list(self):
        """Get count of vertices"""
        return [RegularPoly(vert, RegularPolySeq.radius) for vert in range(3,self.vert_count)]


    def __getitem__(self, seq):
        """get next item in the sequence"""
        if isinstance(seq, int):
            if seq < 0 or seq >self.vert_count:
                raise IndexError
            else:
                return poly_list[seq]

    def __len__(self):
        """get length of sequence"""
        return self.vert_count - 2

    def __str__(self):
        """String represnetation"""
        return f"Polygon sequence with seq_len = {self.vert_count - 2} and common cirum_radius = {self.radius}"

    def __repr__(self):
        """ Return string for RegularPolySeq"""
        return (f'RegularPolySeq({self.vert_count}, {self.radius})')

#     @property
#     def max_efficiency_poly(self):
# #         ratio = -100.0
# #         max_ratio_polygon = None
# #         for i in range(3, self.vert_count + 1):
# #             print(self[i])
# #             poly = self[i]
# #             area_perimeter_ratio = poly.area / poly.perimeter
# #             if area_perimeter_ratio > ratio:
# #                 ratio = area_perimeter_ratio
# #                 max_ratio_polygon = poly
#         sorted(self[i], lambda x: self[i])
#         return max_ratio_polygon

    @staticmethod
    @lru_cache(2**10)
    def _poly(n):
        if n == 3:
            return RegularPoly(n,RegularPolySeq.radius)
        else:
#             return RegularPoly(n,RegularPolySeq.radius), RegularPolySeq._poly(n-1)
            return RegularPolySeq._poly(n-1)
