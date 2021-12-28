from matplotlib import pyplot as plt

# data
unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]

# side by side bars - function

def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]
    # n = select graph number (<= t)
    # t = number of datasets
    # w = width of each bar
    # d = number of sets of bars (columns)
