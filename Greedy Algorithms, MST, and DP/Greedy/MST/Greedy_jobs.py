def read_file(file):
    """read the file, return the jobs and total job count
    jobs are  lists inside of a list with format of ['weight','length']
    """
    jobs = []
    with open(file) as file:
        for position, lines in enumerate(file):
            if position != 0:
                jobs.append([int(x) for x in lines.split()])
            if position == 0:
                nums_jobs = int(lines)
    return jobs, nums_jobs


def schedule_jobs(jobs, score_type):
    """run the greedy algorithm that schedules jobs, return the sum of weighted completion times of the resulting schedule 

    if scocre type == diff: run jobs in decreasing order of the difference (weight - length)
        Recall from lecture that this algorithm is not always optimal.
        IMPORTANT: if two jobs have equal difference (weight - length), you should schedule the job with higher weight first. 
    if score_type == ratio:
        un the greedy algorithm that schedules jobs (optimally) in decreasing order of the ratio (weight/length).
        In this algorithm, it does not matter how you break ties.
    """
    # calculate the priority score
    if score_type == 'diff':
        for job in jobs:
            score_diff = job[0]-job[1]
            job.append(score_diff)
        # sort by score, then weight
        jobs.sort(key=lambda x: (x[2], x[0]), reverse=True)

    if score_type == 'ratio':
        for job in jobs:
            score_ratio = job[0]/job[1]
            job.append(score_ratio)
        # sort by score
        jobs.sort(key=lambda x: (x[2]), reverse=True)

    len_sum = 0
    weighted_time_sum = 0
    for wls in jobs:
        len_sum += wls[1]
        weighted_time_sum += wls[0]*len_sum

    return weighted_time_sum
    #score_weight = job[0]/job[1]


if __name__ == "__main__":
    # jobs, nums_jobs = read_file(
    #     'Greedy Algorithms, MST, and DP/Greedy/MST/jobs.txt')
    # time_sum_diff = schedule_jobs(jobs, 'diff')
    # print(time_sum_diff)

    jobs, nums_jobs = read_file(
        'Greedy Algorithms, MST, and DP/Greedy/MST/jobs.txt')
    time_sum_ratio = schedule_jobs(jobs, 'ratio')
    print(time_sum_ratio)

