# 直接拉你阿里云已推送好的基础镜像，不用重复装依赖
FROM crpi-sttdf1vp2rt3wy5e.cn-shanghai.personal.cr.aliyuncs.com/automation-test-basic/python-3.11-basic:v1.0

WORKDIR /workspace
COPY . .
CMD ["python"]