from flask import Flask, render_template, redirect, url_for, session, request


app = Flask(__name__)
app.secret_key = "iso9001-secret"

USERS = {
    "admin": "aurora123",
    "auditor": "audit42001"
}

ISO_9001_MENU = {

    "4.1 Understanding the organization and its context": [
        "Have internal issues relevant to the QMS been determined?",
        "Have external issues relevant to the QMS been determined?",
        "Is information about these issues monitored and reviewed?"
    ],

    "4.2 Needs and expectations of interested parties": [
        "Have relevant interested parties been identified?",
        "Have the requirements of interested parties been determined?",
        "Are these requirements monitored and reviewed?",
        "Have statutory and regulatory requirements been identified?"
    ],

    "4.3 Scope of the quality management system": [
        "Is the scope of the QMS defined?",
        "Does the scope consider internal and external issues?",
        "Does the scope consider requirements of interested parties?",
        "Is the scope documented and available?"
    ],

    "4.4 Quality management system and its processes": [
        "Have QMS processes been determined?",
        "Are process inputs and outputs defined?",
        "Are process interactions defined?",
        "Are criteria and methods established for processes?",
        "Are responsibilities and authorities assigned?",
        "Is documented information maintained to support processes?"
    ],

    "5.1 Leadership and commitment": [
        "Does top management demonstrate leadership and commitment to the QMS?",
        "Does top management promote a process approach and risk-based thinking?",
        "Does top management ensure customer focus?",
        "Are QMS requirements integrated into business processes?"
    ],

    "5.2 Quality policy": [
        "Is a quality policy established?",
        "Is the policy appropriate to the organization’s purpose and context?",
        "Does the policy provide a framework for quality objectives?",
        "Does the policy include a commitment to meeting requirements?",
        "Does the policy include a commitment to continual improvement?",
        "Is the policy documented, communicated, and understood?"
    ],

    "5.3 Organizational roles, responsibilities, and authorities": [
        "Are roles and responsibilities for the QMS defined?",
        "Are authorities communicated within the organization?",
        "Is responsibility assigned for ensuring QMS conformity?",
        "Is responsibility assigned for reporting QMS performance?"
    ],

    "6.1 Actions to address risks and opportunities": [
        "Have risks and opportunities affecting the QMS been identified?",
        "Have actions been planned to address these risks and opportunities?",
        "Are actions integrated into QMS processes?",
        "Is the effectiveness of these actions evaluated?"
    ],

    "6.2 Quality objectives and planning to achieve them": [
        "Have quality objectives been established?",
        "Are quality objectives measurable?",
        "Are objectives consistent with the quality policy?",
        "Are objectives communicated?",
        "Is planning performed to achieve quality objectives?",
        "Is progress toward objectives monitored?"
    ],

    "6.3 Planning of changes": [
        "Are changes to the QMS planned in a controlled manner?",
        "Are the purpose and consequences of changes considered?",
        "Are resources allocated for changes?",
        "Are responsibilities for changes defined?"
    ],

    "7.1 Resources": [
        "Are resources required for the QMS determined?",
        "Are resources provided to maintain and improve the QMS?",
        "Is infrastructure adequate?",
        "Is the work environment suitable for process operation?"
    ],

    "7.2 Competence": [
        "Is required competence for personnel determined?",
        "Are personnel competent based on education, training, or experience?",
        "Are actions taken to address competence gaps?",
        "Is the effectiveness of competence actions evaluated?",
        "Are competence records maintained?"
    ],

    "7.3 Awareness": [
        "Are personnel aware of the quality policy?",
        "Are personnel aware of quality objectives?",
        "Are personnel aware of their contribution to QMS effectiveness?",
        "Are personnel aware of consequences of nonconformity?"
    ],

    "7.4 Communication": [
        "Are internal and external communication requirements determined?",
        "Is it defined what, when, and with whom to communicate?",
        "Are communication responsibilities assigned?",
        "Is communication effectiveness evaluated?"
    ],

    "7.5 Documented information": [
        "Is documented information required by the QMS identified?",
        "Is documented information controlled?",
        "Are documents reviewed and updated as required?",
        "Are records protected and retained appropriately?"
    ],

    "8.1 Operational planning and control": [
        "Are operational processes planned and controlled?",
        "Are acceptance criteria defined?",
        "Are changes to operations reviewed and controlled?",
        "Is documented information retained to demonstrate conformity?"
    ],

    "8.2 Requirements for products and services": [
        "Are customer requirements determined?",
        "Are statutory and regulatory requirements identified?",
        "Are requirements reviewed prior to commitment?",
        "Are changes to requirements controlled?"
    ],

    "8.3 Design and development of products and services": [
        "Is the design and development process planned and controlled?",
        "Are design inputs defined and reviewed?",
        "Are design outputs defined and approved?",
        "Are design changes identified and controlled?"
    ],

    "8.4 Control of externally provided processes, products, and services": [
        "Are external providers evaluated and selected?",
        "Are criteria defined for external provider control?",
        "Is performance of external providers monitored?",
        "Is verification of externally provided outputs performed?"
    ],

    "8.5 Production and service provision": [
        "Are production and service activities carried out under controlled conditions?",
        "Are work instructions available where necessary?",
        "Is identification and traceability ensured where required?",
        "Is property belonging to customers or external providers protected?",
        "Is preservation of outputs ensured?"
    ],

    "8.6 Release of products and services": [
        "Are release criteria defined?",
        "Is verification performed prior to release?",
        "Is evidence of conformity retained?",
        "Is authorization for release defined?"
    ],

    "8.7 Control of nonconforming outputs": [
        "Are nonconforming outputs identified?",
        "Are nonconforming outputs controlled?",
        "Are actions taken to address nonconformity?",
        "Are records of nonconforming outputs maintained?"
    ],

    "9.1 Monitoring, measurement, analysis, and evaluation": [
        "Is it determined what needs to be monitored and measured?",
        "Are monitoring and measurement methods defined?",
        "Are results analyzed and evaluated?",
        "Are performance trends identified?"
    ],

    "9.1.2 Customer satisfaction": [
        "Is customer perception monitored?",
        "Is feedback collected and analyzed?",
        "Are actions taken based on customer feedback?"
    ],

    "9.2 Internal audit": [
        "Is an internal audit program established?",
        "Are audits planned and conducted at planned intervals?",
        "Are auditors impartial and competent?",
        "Are audit results documented?",
        "Are corrective actions taken without undue delay?"
    ],

    "9.3 Management review": [
        "Are management reviews conducted at planned intervals?",
        "Are required inputs to management review considered?",
        "Are outputs of management review documented?",
        "Are improvement actions assigned and tracked?"
    ],

    "10.2 Nonconformity and corrective action": [
        "Are nonconformities identified and addressed?",
        "Are root causes determined?",
        "Are corrective actions implemented?",
        "Is effectiveness of corrective actions reviewed?",
        "Are records maintained?"
    ],

    "10.3 Continual improvement": [
        "Are opportunities for improvement identified?",
        "Are improvements implemented?",
        "Is QMS effectiveness continually improved?"
    ]
}


ISO_42001_MENU = {

    "4.1 Understanding the organization and its context": [
        "Internal and external issues related to AI identified",
        "Technological, legal, ethical, and societal factors considered",
        "Organization’s role in the AI value chain defined"
    ],

    "4.2 Needs and expectations of interested parties": [
        "Relevant interested parties identified",
        "AI-related expectations and concerns identified",
        "Legal, regulatory, and ethical requirements determined"
    ],

    "4.3 Scope of the AI management system": [
        "AIMS scope defined",
        "AI systems and lifecycle stages specified",
        "Scope documented and available"
    ],

    "4.4 AI management system": [
        "AI management system established",
        "AI governance processes defined",
        "Interactions between AIMS processes defined"
    ],

    "5.1 Leadership and commitment": [
        "Top management commitment to responsible AI demonstrated",
        "AI risks considered in strategic decisions",
        "AI governance responsibilities assigned"
    ],

    "5.2 AI policy": [
        "AI policy established",
        "Ethical AI principles addressed",
        "Legal compliance commitment included",
        "Policy communicated and understood"
    ],

    "5.3 Roles, responsibilities, and authorities": [
        "AI-related roles defined",
        "Accountability for AI decisions assigned",
        "Escalation paths for AI incidents defined"
    ],

    "6.1 Actions to address AI risks and opportunities": [
        "AI risks identified across lifecycle",
        "Potential harms assessed",
        "Risk mitigation measures implemented",
        "AI opportunities evaluated responsibly"
    ],

    "6.2 AI objectives and planning": [
        "Measurable AI objectives defined",
        "Objectives include safety and fairness",
        "Progress toward objectives monitored"
    ],

    "6.3 Planning of changes": [
        "AI system changes planned",
        "Impacts assessed before deployment",
        "Change responsibilities assigned"
    ],

    "7.1 Resources": [
        "Resources allocated for AI governance",
        "Tools support AI risk management",
        "Oversight resources provided"
    ],

    "7.2 Competence": [
        "AI roles assigned to competent personnel",
        "AI ethics and risk training provided",
        "Competence documented"
    ],

    "7.3 Awareness": [
        "Employees aware of AI policy",
        "Employees aware of AI risks",
        "Developers aware of ethical AI requirements"
    ],

    "7.4 Communication": [
        "Internal AI communication defined",
        "External AI communication controlled",
        "Users informed of AI system use"
    ],

    "7.5 Documented information": [
        "AI documentation defined and controlled",
        "Risk assessment records maintained",
        "Model and system documentation available"
    ],

    "8.1 AI system lifecycle management": [
        "AI lifecycle stages defined",
        "Controls applied at each lifecycle stage",
        "Lifecycle responsibilities assigned"
    ],

    "8.2 Data management": [
        "Data sources identified",
        "Data quality assessed",
        "Bias and representativeness evaluated",
        "Data protection requirements met"
    ],

    "8.3 AI system design and development": [
        "Design objectives defined",
        "Safety and robustness considered",
        "Model limitations documented",
        "Testing and validation performed"
    ],

    "8.4 AI system deployment": [
        "Deployment criteria defined",
        "Human oversight implemented",
        "Deployment risks assessed"
    ],

    "8.5 AI system operation and monitoring": [
        "System performance monitored",
        "Unintended behaviors detected",
        "Model drift monitored"
    ],

    "8.6 Human oversight": [
        "Human oversight defined",
        "Override mechanisms available",
        "Oversight responsibilities documented"
    ],

    "8.7 Incident management": [
        "AI incidents identified and reported",
        "Incident response procedures defined",
        "Incidents investigated and documented"
    ],

    "8.8 AI system retirement": [
        "Retirement criteria defined",
        "Model and data decommissioned safely",
        "Retirement impacts assessed"
    ],

    "9.1 Monitoring, measurement, analysis, and evaluation": [
        "AI performance metrics defined",
        "Risk and ethical indicators monitored",
        "Evaluation results documented"
    ],

    "9.2 Internal audit": [
        "AIMS audits planned",
        "Auditors competent in AI topics",
        "Audit results documented"
    ],

    "9.3 Management review": [
        "AIMS performance reviewed",
        "AI risks and incidents reviewed",
        "Improvement actions assigned"
    ],

    "10.1 Nonconformity and corrective actions": [
        "AI nonconformities identified",
        "Root causes analyzed",
        "Corrective actions implemented"
    ],

    "10.2 Continual improvement": [
        "AI improvement opportunities identified",
        "Improvements implemented",
        "AIMS effectiveness improved"
    ]
}

ISO_23894_MENU = {

    "4.1 Context and scope": [
        "AI system scope defined for risk management?",
        "Stakeholders and intended use identified?",
        "Risk criteria and risk acceptance defined?"
    ],

    "4.2 Governance and accountability": [
        "Roles and responsibilities for AI risk management assigned?",
        "Decision-making authority for risk treatment defined?",
        "Risk management integrated into organizational governance?"
    ],

    "4.3 Risk management process": [
        "AI risk management process documented and maintained?",
        "Risk identification performed across the AI lifecycle?",
        "Risk analysis evaluates likelihood and impact?",
        "Risk evaluation compares against criteria?",
        "Risk treatment options selected and recorded?"
    ],

    "4.4 Data and model risk": [
        "Data quality and bias risks assessed?",
        "Model robustness and performance risks assessed?",
        "Monitoring plan for drift and degradation defined?"
    ],

    "4.5 Security and safety": [
        "Adversarial threats and misuse scenarios assessed?",
        "Safety risks (harm, misuse) identified and mitigated?",
        "Incident response and reporting process defined?"
    ],

    "4.6 Transparency and explainability": [
        "Transparency needs for users and stakeholders defined?",
        "Explainability requirements documented for key decisions?",
        "Communication of limitations and risks provided?"
    ],

    "4.7 Compliance and ethics": [
        "Regulatory and legal requirements identified?",
        "Ethical principles and policies applied to AI use?",
        "Auditability and documentation maintained?"
    ],

    "4.8 Monitoring and continual improvement": [
        "Ongoing risk monitoring implemented?",
        "Effectiveness of controls reviewed?",
        "Corrective actions tracked and closed?"
    ]
}

ISO_38507_MENU = {

    "4.1 Governance framework": [
        "AI governance objectives and scope defined?",
        "Governance policies approved and communicated?",
        "Governance roles and accountabilities assigned?"
    ],

    "4.2 Strategy and alignment": [
        "AI strategy aligned with organizational objectives?",
        "Risk and value considerations integrated into strategy?",
        "Stakeholders consulted for AI use cases?"
    ],

    "4.3 Lifecycle oversight": [
        "AI lifecycle phases defined and governed?",
        "Approval checkpoints established for deployment?",
        "Change management and retirement processes defined?"
    ],

    "4.4 Risk and assurance": [
        "AI risk management integrated with governance?",
        "Assurance and audit processes established?",
        "Controls monitored for effectiveness?"
    ],

    "4.5 Transparency and accountability": [
        "Decision transparency and explainability requirements defined?",
        "Accountability for outcomes assigned?",
        "Recordkeeping supports traceability?"
    ],

    "4.6 Data and model stewardship": [
        "Data stewardship roles and responsibilities defined?",
        "Model quality, bias, and performance reviewed?",
        "Model documentation and versioning maintained?"
    ],

    "4.7 Ethics and compliance": [
        "Ethical principles applied to AI use?",
        "Legal and regulatory compliance validated?",
        "Third-party AI suppliers governed?"
    ],

    "4.8 Performance and improvement": [
        "AI performance KPIs defined and monitored?",
        "Issues and incidents tracked and resolved?",
        "Continuous improvement actions implemented?"
    ]
}

ISO_22989_MENU = {

    "4.1 Concepts and definitions": [
        "AI system, model, and data terminology documented?",
        "Stakeholders share a common AI vocabulary?",
        "Key AI concepts communicated across teams?"
    ],

    "4.2 AI system lifecycle": [
        "AI lifecycle phases defined and documented?",
        "Data collection, training, evaluation steps described?",
        "Deployment and monitoring practices documented?"
    ],

    "4.3 Data and models": [
        "Data sources and quality attributes documented?",
        "Model types and assumptions recorded?",
        "Model performance metrics defined?"
    ],

    "4.4 Human involvement": [
        "Human roles in AI decision processes defined?",
        "Human oversight requirements documented?",
        "User training and awareness addressed?"
    ],

    "4.5 System properties": [
        "Accuracy, robustness, and reliability criteria defined?",
        "Bias and fairness considerations documented?",
        "Explainability and transparency requirements described?"
    ],

    "4.6 Operational considerations": [
        "Operational environment and constraints defined?",
        "Monitoring, logging, and incident processes described?",
        "Maintenance and update procedures documented?"
    ],

    "4.7 Governance and documentation": [
        "AI documentation maintained for traceability?",
        "Responsibilities for documentation assigned?",
        "Records retained for auditability?"
    ]
}

ISO_42006_MENU = {

    "4.1 System scope and objectives": [
        "AI system scope for compliance documented?",
        "Objectives aligned to organizational AI policies?",
        "Stakeholders and intended users identified?"
    ],

    "4.2 Data and model documentation": [
        "Training and validation datasets documented?",
        "Model design and assumptions recorded?",
        "Evaluation results and limitations documented?"
    ],

    "4.3 Risk and impact assessment": [
        "Risk assessment performed for AI use cases?",
        "Impact on stakeholders evaluated?",
        "Mitigations defined for identified risks?"
    ],

    "4.4 Human oversight and controls": [
        "Human oversight responsibilities assigned?",
        "Override and escalation processes defined?",
        "User guidance and safeguards provided?"
    ],

    "4.5 Transparency and communication": [
        "Transparency requirements communicated to users?",
        "Explainability approach documented where required?",
        "Disclosures about AI use provided?"
    ],

    "4.6 Monitoring and improvement": [
        "Monitoring plan for performance and drift defined?",
        "Incident logging and response procedures established?",
        "Continuous improvement actions tracked?"
    ]
}

def get_state():
    return session.get("state", {})

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/toggle", methods=["POST"])
def toggle():
    question = request.form["question"]
    state = get_state()

    if question not in state:
        state[question] = {"done": False, "comment": ""}

    state[question]["done"] = not state[question]["done"]
    session["state"] = state
    return redirect(url_for("index"))

@app.route("/comment", methods=["POST"])
def comment():
    question = request.form["question"]
    comment = request.form["comment"]

    state = get_state()
    if question not in state:
        state[question] = {"done": False, "comment": ""}

    state[question]["comment"] = comment
    session["state"] = state
    return redirect(url_for("index"))

@app.route("/iso42001")
def iso42001():
    state = session.get("state_42001", {})
    return render_template(
        "iso42001.html",
        menu=ISO_42001_MENU,
        state=state
    )

@app.route("/iso23894")
def iso23894():
    state = session.get("state_23894", {})
    return render_template(
        "iso23894.html",
        menu=ISO_23894_MENU,
        state=state
    )

@app.route("/iso38507")
def iso38507():
    state = session.get("state_38507", {})
    return render_template(
        "iso38507.html",
        menu=ISO_38507_MENU,
        state=state
    )

@app.route("/iso22989")
def iso22989():
    state = session.get("state_22989", {})
    return render_template(
        "iso22989.html",
        menu=ISO_22989_MENU,
        state=state
    )

@app.route("/iso42006")
def iso42006():
    state = session.get("state_42006", {})
    return render_template(
        "iso42006.html",
        menu=ISO_42006_MENU,
        state=state
    )

@app.route("/toggle42006", methods=["POST"])
def toggle42006():
    question = request.form["question"]
    state = session.get("state_42006", {})

    if question not in state:
        state[question] = {"done": False, "comment": ""}

    state[question]["done"] = not state[question]["done"]
    session["state_42006"] = state
    return redirect(url_for("iso42006"))


@app.route("/comment42006", methods=["POST"])
def comment42006():
    question = request.form["question"]
    comment = request.form["comment"]

    state = session.get("state_42006", {})
    if question not in state:
        state[question] = {"done": False, "comment": ""}

    state[question]["comment"] = comment
    session["state_42006"] = state
    return redirect(url_for("iso42006"))

@app.route("/toggle22989", methods=["POST"])
def toggle22989():
    question = request.form["question"]
    state = session.get("state_22989", {})

    if question not in state:
        state[question] = {"done": False, "comment": ""}

    state[question]["done"] = not state[question]["done"]
    session["state_22989"] = state
    return redirect(url_for("iso22989"))


@app.route("/comment22989", methods=["POST"])
def comment22989():
    question = request.form["question"]
    comment = request.form["comment"]

    state = session.get("state_22989", {})
    if question not in state:
        state[question] = {"done": False, "comment": ""}

    state[question]["comment"] = comment
    session["state_22989"] = state
    return redirect(url_for("iso22989"))

@app.route("/toggle38507", methods=["POST"])
def toggle38507():
    question = request.form["question"]
    state = session.get("state_38507", {})

    if question not in state:
        state[question] = {"done": False, "comment": ""}

    state[question]["done"] = not state[question]["done"]
    session["state_38507"] = state
    return redirect(url_for("iso38507"))


@app.route("/comment38507", methods=["POST"])
def comment38507():
    question = request.form["question"]
    comment = request.form["comment"]

    state = session.get("state_38507", {})
    if question not in state:
        state[question] = {"done": False, "comment": ""}

    state[question]["comment"] = comment
    session["state_38507"] = state
    return redirect(url_for("iso38507"))

@app.route("/toggle23894", methods=["POST"])
def toggle23894():
    question = request.form["question"]
    state = session.get("state_23894", {})

    if question not in state:
        state[question] = {"done": False, "comment": ""}

    state[question]["done"] = not state[question]["done"]
    session["state_23894"] = state
    return redirect(url_for("iso23894"))


@app.route("/comment23894", methods=["POST"])
def comment23894():
    question = request.form["question"]
    comment = request.form["comment"]

    state = session.get("state_23894", {})
    if question not in state:
        state[question] = {"done": False, "comment": ""}

    state[question]["comment"] = comment
    session["state_23894"] = state
    return redirect(url_for("iso23894"))

@app.route("/toggle42001", methods=["POST"])
def toggle42001():
    question = request.form["question"]
    state = session.get("state_42001", {})

    if question not in state:
        state[question] = {"done": False, "comment": ""}

    state[question]["done"] = not state[question]["done"]
    session["state_42001"] = state
    return redirect(url_for("iso42001"))


@app.route("/comment42001", methods=["POST"])
def comment42001():
    question = request.form["question"]
    comment = request.form["comment"]

    state = session.get("state_42001", {})
    if question not in state:
        state[question] = {"done": False, "comment": ""}

    state[question]["comment"] = comment
    session["state_42001"] = state
    return redirect(url_for("iso42001"))

@app.route("/iso9001")
def iso9001():
    state = session.get("state", {})
    return render_template(
        "iso9001.html",
        menu=ISO_9001_MENU,
        state=state
    )

@app.route("/toggle9001", methods=["POST"])
def toggle9001():
    question = request.form["question"]
    state = session.get("state", {})

    if question not in state:
        state[question] = {"done": False, "comment": ""}

    state[question]["done"] = not state[question]["done"]
    session["state"] = state
    return redirect(url_for("iso9001"))


@app.route("/comment9001", methods=["POST"])
def comment9001():
    question = request.form["question"]
    comment = request.form["comment"]

    state = session.get("state", {})
    if question not in state:
        state[question] = {"done": False, "comment": ""}

    state[question]["comment"] = comment
    session["state"] = state
    return redirect(url_for("iso9001"))

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in USERS and USERS[username] == password:
            session["username"] = username
            return redirect(url_for("dashboard"))
        else:
            error = "Invalid username or password"

    return render_template("login.html", error=error)


@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    success = None

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        if not username or not password:
            error = "Username and password are required"
        elif username in USERS:
            error = "Username already exists"
        elif password != confirm_password:
            error = "Passwords do not match"
        else:
            USERS[username] = password
            success = "Account created. Please log in."

    return render_template("register.html", error=error, success=success)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        return redirect(url_for("login"))

    iso9001_state = session.get("state", {})
    iso42001_state = session.get("state_42001", {})
    iso23894_state = session.get("state_23894", {})
    iso38507_state = session.get("state_38507", {})
    iso22989_state = session.get("state_22989", {})
    iso42006_state = session.get("state_42006", {})

    def calculate_stats(state, menu):
        total = sum(len(v) for v in menu.values())
        completed = sum(1 for q in state.values() if q.get("done"))
        percent = int((completed / total) * 100) if total else 0
        return {
            "total": total,
            "completed": completed,
            "open": total - completed,
            "percent": percent
        }

    iso9001_stats = calculate_stats(iso9001_state, ISO_9001_MENU)
    iso42001_stats = calculate_stats(iso42001_state, ISO_42001_MENU)
    iso23894_stats = calculate_stats(iso23894_state, ISO_23894_MENU)
    iso38507_stats = calculate_stats(iso38507_state, ISO_38507_MENU)
    iso22989_stats = calculate_stats(iso22989_state, ISO_22989_MENU)
    iso42006_stats = calculate_stats(iso42006_state, ISO_42006_MENU)

    return render_template(
        "dashboard.html",
        iso9001=iso9001_stats,
        iso42001=iso42001_stats,
        iso23894=iso23894_stats,
        iso38507=iso38507_stats,
        iso22989=iso22989_stats,
        iso42006=iso42006_stats,
        username=session["username"]
    )


if __name__ == "__main__":
    app.run(debug=True)
