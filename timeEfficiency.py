def timeEfficiency(funcName, *args, **kwargs):
    start_time = time.perf_counter()

    result = funcName(*args, **kwargs)

    end_time = time.perf_counter()

    elapsed_time = end_time - start_time

    print(f"""
    List of prime numbers of {args[0]} {{
        'start': {start_time}, 'end': {end_time}, 'time efficiency': {elapsed_time}
        'result': {result}
    }} # edited for nicer look
    """)
