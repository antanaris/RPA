# Logic for submitting a testcase
    # each time it is called it generates next_steps.json (it can contain several steps)
    # if there are no steps to execute, the next_steps.json should be empty

# input parameters
    # testcase ID
    # status: Passed
    # assign_To: Me
    # version: 0.1
    # elapsed: 15m
    # defects
    # comment

# Logic is
#   set status (default Passed)
#   add a comment if any
#   pass all steps (if any) by tapping on the green P (Set all steps to "Passed".)
#   assign to Me
#   add version (default 0.1)
#   add elapsed time (default 15m)
#   add defects if any


# return => next_steps.json