F = 4 * 8e9              # bits
us = 100e6; di = 50e6; ui = 20e6; N = 20
T_cs  = max(N*F/us, F/di)                    # 6400 s
T_p2p = max(F/us, F/di, N*F/(us + N*ui))     # 1280 s
print(f"Client-server: {T_cs/60:.1f} min")   # 106.7
print(f"P2P:           {T_p2p/60:.1f} min")  # 21.3