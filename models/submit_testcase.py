# Writes down next steps for submitting a testcase
    # each time it is called it generates next_steps.json
    # if there are no steps to execute, the next_steps.json should be empty

# input parameters
    # testrun ID
    # testcase ID
    # status: Passed
    # assign_To: Me
    # version: 0.1
    # elapsed: 15m
    # defects
    # comment

# Logic is
#   press on the arrow on the very right of the test case
#   press + Add Result button
#   in the opened popup
    #   set status (default Passed)
    #   add a comment if any
    #   pass all steps (if any) by tapping on the green P (Set all steps to "Passed".)
    #   Add (random) actual results for each step
    #   assign to Me
    #   add version (default 0.1)
    #   add elapsed time (default 15m)
    #   add defects if any


# return => next_steps.json