# process vs thread

# - to answer this lets understand what a program is
# - A program is a set of instructions that a computer can execute. and is stored as a file on disk
# - when the code in the program is loaded into memory and executed by the CPU, it is called a process.
# - A process is an instance of a program that is being executed. It has its own memory space and resources.
# - A process can have multiple threads, which are smaller units of execution within the process.

# - Threads share the same memory space and resources of the process, but can execute independently.
# - Threads are lighter than processes and can be created and destroyed more quickly.
# -  Threads have registers, stack, and program counter.

# how does os manage processes and threads?
# - The operating system (OS) is responsible for managing processes and threads.
# - The OS uses a scheduler to allocate CPU time to processes and threads.
# - The scheduler determines which process or thread should run at any given time.
# - The OS also manages memory allocation and deallocation for processes and threads.
# - The OS provides system calls for creating, terminating, and managing processes and threads.

# context switching
# - Context switching is the process of saving the state of a running process or thread and restoring the state of
# another process or thread.


# Concurrency vs Prallelism
# - Concurrency is the ability of a program to execute multiple tasks simultaneously.
# - Parallelism is the ability of a program to execute multiple tasks simultaneously on multiple processors.
# - Concurrency is achieved through multi-threading or multi-processing.
# - Parallelism is achieved through multi-processing or distributed computing.
# - example of concurrency: a web server that can handle multiple requests at the same time.
# - example of parallelism: a program that can process large data sets using multiple processors.



