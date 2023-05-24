from bananopie import *
import time

rpc = RPC("https://public.node.jungletv.live/rpc", legacy=True)

print("RPC and utils test")

start_time = time.time()
print(rpc.get_block_count()["count"])
print(f"Elapsed time: {round(time.time() - start_time, 2)} seconds")

start_time = time.time()
print(rpc.get_account_history("ban_1jung1eb3uomk1gsx7w6w7toqrikxm5pgn5wbsg5fpy96ckpdf6wmiuuzpca", count=10)["history"][0])
print(f"Elapsed time: {round(time.time() - start_time, 2)} seconds")

start_time = time.time()
print(raw_to_whole(int(rpc.get_account_balance("ban_1jung1eb3uomk1gsx7w6w7toqrikxm5pgn5wbsg5fpy96ckpdf6wmiuuzpca")["balance"])))
print(f"Elapsed time: {round(time.time() - start_time, 2)} seconds")

print("Wallets test")
start_time = time.time()
my_account = Wallet(rpc, seed="3AB019DFCBA0B3763A75B8717EE7900911C7DD4E3B6E31FAE8906EDA71521C98", index=0, try_work=True)
print(f"Elapsed time: {round(time.time() - start_time, 2)} seconds")

print("Receive test")
start_time = time.time()
print(my_account.receive_all())
print(f"Elapsed time: {round(time.time() - start_time, 2)} seconds")

print("Send test")
start_time = time.time()
print(my_account.send("ban_3pdripjhteyymwjnaspc5nd96gyxgcdxcskiwwwoqxttnrncrxi974riid94", "0.1"))
print(f"Elapsed time: {round(time.time() - start_time, 2)} seconds")

print("Change test")
start_time = time.time()
print(my_account.change_rep("ban_3catgir1p6b1edo5trp7fdb8gsxx4y5ffshbphj73zzy5hu678rsry7srh8b"))
print(f"Elapsed time: {round(time.time() - start_time, 2)} seconds")

start_time = time.time()
my_account.index = 1
print(f"Elapsed time: {round(time.time() - start_time, 2)} seconds")

start_time = time.time()
print(my_account.receive_all())
print(f"Elapsed time: {round(time.time() - start_time, 2)} seconds")

start_time = time.time()
print(my_account.send("ban_3pdripjhteyymwjnaspc5nd96gyxgcdxcskiwwwoqxttnrncrxi974riid94", "0.0040000501"))
print(f"Elapsed time: {round(time.time() - start_time, 2)} seconds")

no_work_rpc = RPC("https://public.node.jungletv.live/rpc", legacy=True)
#print(no_work_rpc.get_receivable("ban_1mayorbance1ot1sburnedbananas11111111111111111111111zsqrpxj1", count = 1))

#gen_work

#assert verify_work("C6A3732E65800203CE0F32DE710CC110A0CA93C0080F5F0C84A352978DB285F9", "58C5C876832364CC") == True

my_work_account = Wallet(no_work_rpc, seed="3AB019DFCBA0B3763A75B8717EE7900911C7DD4E3B6E31FAE8906EDA71521C98", index=0, try_work=True)
start_time = time.time()
my_work_account.receive_all()

print(f"Elapsed time: {round(time.time() - start_time, 2)} seconds")

start_time = time.time()
my_work_account.send("ban_3pdripjhteyymwjnaspc5nd96gyxgcdxcskiwwwoqxttnrncrxi974riid94", "0.0145")
print(f"Elapsed time: {round(time.time() - start_time, 2)} seconds")