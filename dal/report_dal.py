from typing import Optional
from sqlmodel import Session, select, col
from datetime import date
from models.report import Report


def create_report(session:Session,id :int,create_at:date,information:str,agent_id:int,terorist_id:int):
    report = Report(id=id, agent_id=agent_id,terorist_id=terorist_id,information=information,create_at=create_at)
    session.add(report)
    session.commit()
    session.refresh(report)
    print(f"created report: (ID: {report.id}) (Agent: {report.agent_id}) (Terorist: {report.terorist_id}) (info: {report.information}) (created_at: {report.create_at})")
    return report

def read_report(session:Session):
    statement = select(Report)
    reports = session.exec(statement).all()
    print(f"found {len(reports)} reports:")
    for report in reports:
        print(f"(ID: {report.id}) (Agent: {report.agent_id}) (Terorist: {report.terorist_id}) (info: {report.information}) (created_at: {report.create_at}")
    return reports

def read_report_by_id(session: Session,id:Optional[int]):
    if id is None:
        print("ID cant be none")
        return None
    report = session.get(Report,id)
    if report:
        print(f"report found : (ID: {report.id}) (Agent: {report.agent_id}) (Terorist: {report.terorist_id}) (info: {report.information}) (created_at: {report.create_at}")
    else:
        print(f"report with ID {id} not found")
    return report

def read_report_by_agent(session: Session,agent_id:Optional[int]):
    if agent_id is None:
        print("agent_id cant be none")
        return None
    statement = select(Report).where(Report.agent_id == agent_id)
    reports = session.exec(statement).all()
    if reports:
        print(f" found {len(reports)} reports for agent {agent_id}")
        for report in reports:
            print(f"report found : (ID: {report.id}) (Agent: {report.agent_id}) (Terorist: {report.terorist_id}) (info: {report.information}) (created_at: {report.create_at}")
    else:
        print(f"report with agent_id {agent_id} not found")
    return reports

def read_report_by_terorist(session: Session,terorist_id:Optional[int]):
    if terorist_id is None:
        print("terorist_id cant be none")
        return None
    statement = select(Report).where(Report.terorist_id == terorist_id)
    reports = session.exec(statement).all()
    if reports:
        print(f'found {len(reports)} reports for terorist {terorist_id}')
        for report in reports:
            print(f"report found : (ID: {report.id}) (Agent: {report.agent_id}) (Terorist: {report.terorist_id}) (info: {report.information}) (created_at: {report.create_at}")
    else:
        print(f"report with terorist_id {terorist_id} not found")
    return reports

def read_report_by_time(session: Session,create_at:Optional[date]):
    if create_at is None:
        print("time cant be none")
        return None
    statement = select(Report).where(Report.create_at == create_at)
    reports = session.exec(statement).all()
    if reports:
        print(f"found {len(reports)} reports from date {create_at}")
        for report in reports:
            print(f"report found : (ID: {report.id}) (Agent: {report.agent_id}) (Terorist: {report.terorist_id}) (info: {report.information}) (created_at: {report.create_at}")
    else:
        print(f"report with time {create_at} not found")
    return reports

def read_report_by_info(session:Session,keyword:str):
    statement = select(Report).where(Report.information.contains(keyword))
    reports = session.exec(statement).all()
    if reports:
        print(f"found {len(reports)} reports containing {keyword}")
        for report in reports:
            print(f"report found : (ID: {report.id}) (Agent: {report.agent_id}) (Terorist: {report.terorist_id}) (info: {report.information}) (created_at: {report.create_at}")
    else:
        print(f"report with words {keyword} not found")
    return reports

def deleate_report(session:Session, id: Optional[int]):
    if id is None:
        print("ID cant be None")
        return False
    report = session.get(Report,id)
    if not report:
        print(f"id {id} not found")
        return False
    session.delete(report)
    session.commit()
    print(f"deleate report with id : {report.id}")
    return True