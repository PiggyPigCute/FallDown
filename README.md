# FallDown

**Fall Down** is an esolang using "gravity", the main idea is to use balls that can fall, roll, duplicate themselves, mix with other balls, store a value...
A Fall Down program is executed tick per tick, each teak all the balls move at the same time. Each ball stores a value (of 0 at beggining) that increase by 1 each tick where the ball is falling.

```
.



\         #
 ----------
```

This program output the number 3. Indeed there are 3 lines beetween the start of the ball (`.`) and the first slope (`\`), then the ball is falling during 3 ticks (so it has a value of 3 when it arrives at the slope). Then, due to the slope, the ball is going to roll on the groupd (`-`) until the operand `#` that print the value stored in the ball. Then the ball will be out of the frame of the program, so the ball will disapear and the execution will be done.

```
/+ +  .
 --- ?/
    /
$~-~

/    .
 -~ ?/
 : /   /      .
$-\\    -- ---/
       +  /
   \-~---~
  #
```

This is another example of program that multiply the two inputs.

## Python Executor

The `exe.py` fil is a Fall Dawn executor, to use it, type in the console

```
py exe.py <PATH>
```

with `example.fld` the relative (or not) path to the Fall Down program file.
