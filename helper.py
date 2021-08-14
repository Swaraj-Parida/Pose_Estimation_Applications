def calculate_hand_sign(wrist, thumb_tip, index_tip, middle_tip, ring_tip, pinky_tip, thumb_mcp, index_mcp, middle_mcp,
                        ring_mcp, pinky_mcp):
    """
    SIGNS--> 'YO' 'thumbs up' 'thumbs down' 'call' 'rock' 'paper' 'scissor'
    BASELINE --> the MCP point is the base line for each index
    :param wrist: x, y coordinates
    :param thumb_tip: x, y coordinates
    :param index_tip: x, y coordinates
    :param middle_tip: x, y coordinates
    :param ring_tip: x, y coordinates
    :param pinky_tip: x, y coordinates
    :param thumb_mcp: x, y coordinates
    :param index_mcp: x, y coordinates
    :param middle_mcp: x, y coordinates
    :param ring_mcp: x, y coordinates
    :param pinky_mcp: x, y coordinates
    :return: whatever sign is identified
    """
    ## STATE ~ SIGN
    states = ['YO', 'thumbs up', 'thumbs down', 'call', 'Perfect', 'rock', 'paper', 'scissor']
    state = ''
    dist_middle_finger = ((((middle_tip[0] - middle_mcp[0]) ** 2) + ((middle_tip[1] - middle_mcp[1]) ** 2)) ** 0.5)
    dist_thumb_to_pinky = ((((thumb_tip[0] - pinky_mcp[0]) ** 2) + ((thumb_tip[1] - pinky_mcp[1]) ** 2)) ** 0.5)
    ## For 'YO' sign:
    # index and middle tip are above baseline; ring and pinky tips are below the baseline;
    if index_tip[1] < index_mcp[1] and middle_tip[1] < middle_mcp[1]:
        if ring_tip[1] > ring_mcp[1] and pinky_tip[1] > pinky_mcp[1]:
            if thumb_tip[0]<thumb_mcp[0]:
                state = states[0]
                return state, middle_tip

    ## For 'Thumbs UP' sign
    if thumb_tip[1] < thumb_mcp[1]:
        if thumb_mcp[1]< middle_mcp[1]<ring_mcp[1]< pinky_mcp[1]:
            if index_tip[1] < middle_tip[1] < ring_tip[1] < pinky_tip[1]:
                if index_mcp[1] < middle_mcp[1] < ring_mcp[1] < pinky_mcp[1]:
                    state = states[1]
                    return state, middle_tip

    ## For 'Thumbs DOWN' sign
    if thumb_tip[1] > thumb_mcp[1]:
        if index_tip[1] > middle_tip[1] > ring_tip[1] > pinky_tip[1]:
            if index_mcp[1] > middle_mcp[1] > ring_mcp[1] > pinky_mcp[1]:
                state = states[2]
                return state, middle_tip

    # ## For 'CALL' sign
    # if dist_thumb_to_pinky > 2*dist_middle_finger:
    #     if pinky_tip[1]>pinky_mcp[1]:
    #         state = states[3]
    #         return state

    ## For 'Perfect' sign
    if middle_tip[1] < middle_mcp[1] and ring_tip[1] < ring_mcp[1] and pinky_tip[1] < pinky_mcp[1]:
        if index_tip[1] > index_mcp[1]:
            if (abs(index_tip[0] - thumb_tip[0]) < 5) and (abs(index_tip[1] - thumb_tip[1]) < 5):
                state = states[4]
                return state, middle_tip
    return '', middle_tip

