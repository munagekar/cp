class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False

        while num > 1:
            num, div = divmod(num, 4)
            print(num, div)
            if div != 0:
                return False

        return True

{"message": "predict_inputs", "user_id": "701876326", "user_type": "mercari", "item_name": "レクサスGS", "category_id": 944, "item_condition": 1, "brand_id": 0, "created_time": "2020-08-05T04:07:40", "context_metadata": {"user-agent": "grpc-go/1.29.1", "gateway-x-app-version": "64001", "x-datadog-trace-id": "2845096370219442872", "x-datadog-parent-id": "14022631690004039", "x-datadog-sampling-priority": "1", "gateway-x-platform": "ios", "x-forwarded-proto": "http", "x-request-id": "494e1e0e-a9fb-47aa-9ec7-fa307ff711bc", "x-envoy-decorator-operation": "grpc-server.mercari-ml-price-jp-dev.svc.cluster.local:5000/*", "x-envoy-peer-metadata-id": "sidecar~10.33.31.142~app-server-7f75c9fb8-849vw.mercari-listing-jp-dev~mercari-listing-jp-dev.svc.cluster.local", "x-envoy-expected-rq-timeout-ms": "3599998", "x-b3-traceid": "247b83e5daa40c342726bc3627f7dd92", "x-b3-spanid": "2726bc3627f7dd92", "x-b3-sampled": "0"}, "timestamp": "2020-08-05T04:07:40.787303Z", "level": "INFO", "pathname": "/project/price/serve/grpc.py", "lineno": 101, "env": "development", "request_id": "b04c882f-8dff-4927-b103-8fa4167a8556", "dd.trace_id": 2845096370219442872, "dd.span_id": 14905019950582381314, "service": "mercari-ml-price-jp"}