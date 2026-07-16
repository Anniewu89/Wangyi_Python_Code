

pipeline{
    agent any

    environment{
        String getCode = "Start to get automation test scripts from github.."
        String buildimage = "Start to build docker image.."
        String runTestScripts = "Start to run test scripts.."
        String getTestResult = "Get test result.."
		ACR_HOST = "crpi-sttdf1vp2rt3wy5e.cn-shanghai.personal.cr.aliyuncs.com"
        IMAGE_NAME="${ACR_HOST}/automation-test-basic/test-task:${BUILD_NUMBER}"
    }

    options{
        timestamps() //在每一行的log中都加上时间
        skipDefaultCheckout() //跳过一开始就会去拉仓库的最新代码
        disableConcurrentBuilds() //禁用并行
        timeout(time: 1, unit: 'HOURS')
        ansiColor('xterm')
    }

	stages{

	    // 拉取最新的测试脚本
	    stage("[32m=====1.Get code from github[0m"){
	        steps{
	            timeout(time: 3, unit: "MINUTES") {
	                script {
	                    println(env.getCode)
	                    retry(count:10,sleep:20){
	                        checkout scm
	                    }

	                }

	            }
	        }
	    }

		//登录阿里云私有仓库
		stage('[32m=====2. Login ACR[0m') {
	        steps {
	            withCredentials([usernamePassword(
	                credentialsId: 'aliyun-acr-login',
	                usernameVariable: 'DOCKER_USER',
	                passwordVariable: 'DOCKER_PWD'
	            )]) {
	                bat """
	                    docker login ${ACR_HOST} -u ${DOCKER_USER} -p ${DOCKER_PWD}
	                """
	            }
	        }
        }

		stage("[32m=====3.Build Docker images[0m"){
			steps{
				bat "docker build -t ${IMAGE_NAME} ."

			}
		}

		stage("4. run test scripts at the same time"){
				parallel {
                    // 运行脚本
			        stage("[32m=====4.1.run test scripts[0m"){
				        steps{
				            timeout(time:5, unit:"MINUTES"){
					            script{
					                bat """
					                    md report_task1 2>nul
					                    docker run --rm -v ${WORKSPACE}/report_task1:/workspace/report ${IMAGE_NAME} python run_test.py
					                    timeout /t 2 /nobreak >nul
						                """
					            }


							}
				        }
			        }

					// 运行脚本
			        stage("[32m=====4.2.run test scripts[0m"){
				        steps{
				            timeout(time:5, unit:"MINUTES"){
					            script{
					                bat """
					                    md report_task2 2>nul
					                    docker run --rm -v ${WORKSPACE}/report_task2:/workspace/report ${IMAGE_NAME} python run_test_01.py
						                timeout /t 2 /nobreak >nul
						                """
					            }
							}
				        }
			        }
				}
		}



	}


	//后置处理
	post{

		// 一定会处理的
		always {
	        bat "docker system prune -f"
		        // 任务1报告
		        publishHTML(target: [
		            allowMissing: true,
		            alwaysLinkToLastBuild: true,
		            keepAll: true,
		            reportDir: 'report_task1',
		            reportFiles: 'test_report.html',
		            reportName: '测试任务1报告'  ])
		        // 任务2报告
		        publishHTML(target: [
		            allowMissing: true,
		            alwaysLinkToLastBuild: true,
		            keepAll: true,
		            reportDir: 'report_task2',
		            reportFiles: 'test_report.html',
		            reportName: '测试任务2报告'  ])
         }

		// 构建成功的处理
		success{
			script{
				println("Success")
				currentBuild.description += "\n 构建成功"
			}
		}

		//构建失败的处理
		failure{
			script{
				println("failure")
                currentBuild.description += "\n 构建失败"
			}
		}

		//构建取消的处理
		aborted{
			script{
				println("aborted")
				currentBuild.description += "\n 构建取消"
			}


		}

	}


}