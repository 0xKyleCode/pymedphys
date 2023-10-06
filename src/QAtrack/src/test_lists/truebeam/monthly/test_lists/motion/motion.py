MONTHLY_MOTION_RPM = {
    "long name": "Monthly Motion using RPM System",
    "slug": "monthly-motion-rpm",
    "description": r"""<font color="#0070c0">Plan: <b>10RPM.dcm</b></font>
    <br><b>SETUP:</b> Position RPM phantom on couch with 4-dot marker approximately aligned to isocentre. Activate phantom motion.
      <br><b>ACQUISITION:</b> Use <font color="red"><b>TREATMENT</b></font> mode, file directory: Shared drive\PHYSICS\MachineID\QA\Monthly QA.
      <br> At console, select "Create a new tracking protocol by importing RPM data" from the file ID: viPhysicsQA; select 6-dot marker reference session;
      <br> Accept patient data; Initiate tracking by pressing Start/Stop respiratory tracking icon; Deliver gated treatment. Result status: Pass or Fail.

    """,
    "tests": [
        {"name": "monthly_motion_management_rpm_total_patient_motion"},
        {"name": "monthly_motion_management_rpm_gated_residual_motion"},
        {"name": "monthly_motion_management_rpm_total_cycle_period"},
        {"name": "monthly_motion_management_rpm_total_beam_on"},
        {"name": "monthly_motion_management_rpm_time_delay"},
        {"name": "monthly_motion_management_rpm_beam_on"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}

MONTHLY_MOTION_ALL = {
    "long name": "Monthly Motion",
    "slug": "monthly-motion",
    "description": r"""<font color="#0070c0">Plan: <b>10RPM.dcm</b></font>
    <br><b>SETUP:</b> Position RPM phantom on couch with 4-dot marker approximately aligned to isocentre. Activate phantom motion.
      <br><b>ACQUISITION:</b> Use <font color="red"><b>TREATMENT</b></font> mode, file directory: Shared drive\PHYSICS\MachineID\QA\Monthly QA.
      <br> At console, select "Create a new tracking protocol by importing RPM data" from the file ID: viPhysicsQA; select 6-dot marker reference session;
      <br> Accept patient data; Initiate tracking by pressing Start/Stop respiratory tracking icon; Deliver gated treatment. Result status: Pass or Fail.

    """,
    "tests": [],
    "test_lists": [{"name": MONTHLY_MOTION_RPM, "order": 0}],
    "sublists": [],
    "cycle": [],
}

MONTHLY_MOTION = {
    "long name": "Monthly Motion",
    "slug": "monthly-motion",
    "description": "Monthly Motion",
    "tests": [],
    "test_lists": [],
    "sublists": [{"name": MONTHLY_MOTION_ALL}],
    "cycle": [],
}
