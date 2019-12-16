from libc.math cimport ceil
from cpython cimport array


cdef array.array[int] _calculate_fft(input_array: array.array[int]):
    cdef array.array output_array = array.clone(input_array, len(input_array), True)
    cdef int length = len(input_array)
    cdef int i = 1
    cdef array.array pattern
    cdef int index, total
    while i < length + 1:
        pattern = array.array('b')
        index = 1
        while index < length + 1:
            if index/i % 4 == 0:
                pattern.append(0)
            if index/i % 4 == 1:
                pattern.append(1)
            if index/i % 4 == 2:
                pattern.append(0)
            if index/i % 4 == 3:
                pattern.append(-1)
            index += 1
        total = 0
        index = 0
        while index < length:
            total += input_array[index] * pattern[index]
            index += 1
        total = abs(total)
        total %= 10
        output_array[i-1] = total
        i+=1
    return output_array

cpdef array.array[int] calculate_fft(input_array: array.array[int]):
    return _calculate_fft(input_array)
