from collections import defaultdict
cimport cython

#ctypedef int (*inp)()
#ctypedef void (*out)(int)

cdef void _print(int i):
    print(i)

cdef int _input():
    return int(input("Program is requesting input\n>>> "))

@cython.freelist(8)
cdef class InfiniteTape:
    def __init__(self, items):
        self.data = defaultdict(int)
        for index, i in enumerate(items):
            self.data[index] = i

    def __getitem__(self, key):
        if isinstance(key, slice):
            return [self.data[i] for i in range(key.start, key.stop)]
        else:
            return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

@cython.freelist(8)
cdef class IP:
    cdef int address
    def __init__(self):
        self.address = 0

    cdef set(self, new_address):
        self.address = new_address

    cdef int get(self):
        return self.address

ctypedef void (*op)(Computer, Address, Address, Address)

@cython.freelist(32)
cdef class Address:
    cdef InfiniteTape tape
    cdef int location
    def __init__(self, tape: InfiniteTape, initial_address: int):
        self.tape = tape
        self.location = self.tape[initial_address]

    cdef resolve_to_address(self):
        self.value = self.tape[self.location]

    cdef resolve_to_value(self):
        self.value = self.location

    cdef resolve_to_relative(self, relative_base: int):
        self.location += relative_base
        self.resolve_to_address()

    cdef write(self, data: int):
        self.tape[self.location] = data

@cython.freelist(8)
cdef class Computer:
    cdef InfiniteTape tape
    cdef IP ip
    #cdef inp in_function
    #cdef out out_function
    cdef int relative_base
    cpdef bint halted
    cdef int last_instruction
    cdef op instructions[10]
    cdef int arg_no[10]
    arg_no = [0, 3, 3, 1, 1, 2, 2, 3, 3, 1]
    instructions = [
        add,
        add,
        mul,
        take_input,
        output,
        jnz,
        jz,
        tlt,
        teq,
        mod_base,
    ]
    def __init__(
        self,
        data: str,
        #inp in_function = _input,
        in_function = _input,
        #out out_function = _print,
        out_function = _print,
        relative_base: int = 0,
    ):
        self.tape = InfiniteTape(int(i) for i in data.split(","))
        self.ip = IP()

        self.in_function = in_function
        self.out_function = out_function

        self.relative_base = relative_base
        self.halted = False
        self.last_instruction = -1

    cpdef run_until_instruction(self, opcode: int):
        self.eval_one_instruction()
        while not (self.last_instruction == opcode or self.halted):
            self.eval_one_instruction()

    @property
    def next_instruction(self):
        return self.tape[self.ip.get()] % 100

    cpdef eval_one_instruction(self):
        if self.halted:
            return
        cdef int ip = self.ip.get()
        cdef int opcode = self.tape[ip]
        cdef int param_modes = opcode // 100
        opcode = opcode % 100
        #param_modes, opcode = divmod(opcode, 100)
        self.last_instruction = opcode
        if opcode == 99:
            self.halted = True
            return
        cdef list parameters = [None,None,None]
        cdef int i
        try:
            for i in range(3):
                parameters[i] = Address(self.tape, ip + 1 + i)
        except:
            print(ip, param_modes, opcode)
            self.halted = True
            raise StopIteration
        cdef str param_str = str(param_modes).zfill(self.arg_no[opcode])[::-1]
        self.ip.set(ip + self.arg_no[opcode] + 1)
        cdef Address param
        cdef str mode
        cdef position
        for position in range(3):
        #for param, mode in zip(parameters, param_str):
            param = parameters[position]
            mode = param_str[position]
            if mode == '0':
                param.resolve_to_address()
            if mode == '1':
                param.resolve_to_value()
            if mode == '2':
                param.resolve_to_relative(self.relative_base)
        self.instructions[opcode](self, parameters[0], parameters[1], parameters[2])

    cpdef run_until_complete(self):
        while not self.halted:
            self.eval_one_instruction()

    cdef void add(self, a: Address, b: Address, c: Address):
        c.write(a.value + b.value)

    cdef void mul(self, a: Address, b: Address, c: Address):
        c.write(a.value * b.value)

    cdef void take_input(self, a: Address, b: Address, c: Address):
        a.write(self.in_function())

    cdef void output(self, a: Address, b: Address, c: Address):
        self.out_function(a.value)

    cdef void jnz(self, a: Address, b: Address, c: Address):
        if a.value:
            self.ip.set(b.value)

    cdef void jz(self, a: Address, b: Address, c: Address):
        if not a.value:
            self.ip.set(b.value)

    cdef void tlt(self, a: Address, b: Address, c: Address):
        c.write(int(a.value < b.value))

    cdef void teq(self, a: Address, b: Address, c: Address):
        c.write(int(a.value == b.value))

    cdef void mod_base(self, a: Address, b: Address, c: Address):
        self.relative_base += a.value


if __name__ == "__main__":
    tape = input("Enter the program\n>>> ")
    computer = Computer(tape)
    computer.run_until_complete()
