from collections import deque
import sys

bucket_set = set()
answer_set = set()
q = deque()

def run_bucket(bucket_a, bucket_b, bucket_c):
    global bucket_set


bucket_a, bucket_b, bucket_c = tuple(map(int, sys.stdin.readline().split()))

run_bucket(bucket_a, bucket_b, bucket_c)