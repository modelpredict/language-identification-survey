from benchmarks import BENCHMARKS


if __name__ == "__main__":
  mem_usage = {}
  for benchmark_name in BENCHMARKS:
    mem_usage[benchmark_name] = BENCHMARKS[benchmark_name]['measure_memory']()
  print(mem_usage)
