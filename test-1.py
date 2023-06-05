from locust import HttpUser, FastHttpUser, task

class QuickstartUser(FastHttpUser):

    @task
    def getBalance(self):
        payload = {"jsonrpc":"2.0", "method":"eth_getBalance", "params":["0xFE3B557E8Fb62b89F4916B721be55cEb828dBd73", "latest"], "id":2018}
        with self.client.post("/", name="get balance", json=payload, catch_response=True) as response:
            if response.status_code == 200 and "result" in response.text and "0x" in response.text:
                response.success()
            else:
                response.failure(f'Failed: {response.text}')

    @task
    def getBlockNumber(self):
        with self.client.post("/", name="get block number", json={"jsonrpc": "2.0", "method": "eth_blockNumber", "id": 2018}, catch_response=True) as response:
            if response.status_code == 200 and "result" in response.text and "0x" in response.text:
                response.success()
            else:
                response.failure(f'Failed: {response.text}')
